from  tradeutil import time_sleep
import datetime
import time

#instantiate the class
tsc = time_sleep.time_sleep_calculator()
#time sleep calculates the seconds remaining until the next interval referenced to 00:00
#e.g 5mins intervals at 00:00, 00:05, 00:10 etc
tsc.time_sleep(datetime.datetime.now(), interval = '1min')

#confirm calculated time until next interval
print(f"Waiting {tsc.time_sleep_final} Seconds, Time: {datetime.datetime.now()}")

#wait the calculated interval in seconds and visually confirm that activated time is correct
time.sleep(tsc.time_sleep_final)
print(f"{tsc.time_sleep_final} Seconds Elapsed, Time: {datetime.datetime.now()}")