# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:00:07 2023

@author: jaggs
"""


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os
import re


def email_out(sender_address = None,
              sender_pass = None,
              receiver_address = None,
              receiver_address_cc = None,
              receiver_address_bcc = None,
              message_title = None,
              message_text = None,
              message_attachments = None,
              message_images = None):
    '''
    (dict)->(int)(string)(smptlib obj)
    Function to send an email from a gmail account

    Requires the following dictionary keys passed at runtime
    sender_address = "sender@gmail.com",*
    sender_pass = "123456789",*
    receiver_address = ["receiver@yahoo.co.uk"],*
    receiver_address_cc = ["receiver@yahoo.co.uk"],*
    receiver_address_bcc = ["receiver@yahoo.co.uk"],*
    message_title = "A string",*
    message_text = "A string",
    message_attachments = [list of file paths],


    * indicates required input

    Returns integer code
    101 = No message title
    102 = invalid email fomats detected
    200 = message sent with no errors
    '''

    #create message
    msg = MIMEMultipart()


    #check sender email address is present and contains a plausible email string format
    if sender_address is None:
        return 101, "No Sender Email Addresses Supplied"
    if not isValidEmail(sender_address):
        return 101, f"Invalid Sender Email String Format {sender_address}"

    #check sender email password is present
    if sender_pass is None:
        return 101, "No Sender Email Password Supplied"

    #check message title is present, convert to string if not in correct format
    if message_title == None or message_title == "":
        return 101, "No Message Title Supplied"
    elif not isinstance(message_title,str):
        message_title = str(message_title)
    
    #check main message is a string
    if not isinstance(message_text,str):
        message_text = str(message_text)

    #check receiver email addresses supplied and each contains a plausible email string format
    if receiver_address is None:
        return 101, f"No Receiver Emails Supplied"
    for r_email_address in receiver_address:
        if not isValidEmail(r_email_address):
            return 102, f"Invalid Email String Format {r_email_address}"   
    
    #if not empty check each cc email addresses contains a plausible email string format
    if receiver_address_cc is not None:
       for cc_email_address in receiver_address_cc:
            if not isValidEmail(cc_email_address):
                return 102, f"Invalid Email String Format {cc_email_address}"  
    
    #if not empty check each bcc email addresses contains a plausible email string format
    if receiver_address_bcc is not None:
       for bcc_email_address in receiver_address_bcc:
            if not isValidEmail(bcc_email_address):
                return 102, f"Invalid Email String Format {bcc_email_address}"  

    #populate recipient email addresses
    msg['From'] = sender_address
    msg['Subject'] = message_title
    msg['To'] = ','.join(map(str,receiver_address))
    
    if receiver_address_cc is not None:
        msg['Cc'] = ','.join(map(str,receiver_address_cc))
    if receiver_address_bcc is not None:
        msg['Bcc'] = ','.join(map(str,receiver_address_bcc))
    
    msgText = MIMEText('<b>%s</b>' % (message_text), 'html')
    msg.attach(msgText)

    if message_attachments is not None:
        for attachment in message_attachments:
            print(attachment)
            attach_file = MIMEApplication(open(attachment, 'rb').read())
            attach_file.add_header('Content-Disposition', 'attachment', filename= os.path.basename(attachment))
            msg.attach(attach_file)



    if message_images is not None:
        for image in message_images:
            print(image)

            with open(image, "rb") as fp:
                img = MIMEImage(fp.read())
                img.add_header("Content-ID", "<{}>".format(os.path.basename(image)))
                msg.attach(img)


    
    try:
        with smtplib.SMTP('smtp.gmail.com',587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(sender_address, sender_pass)
            smtpObj.sendmail(sender_address, ','.join(map(str,receiver_address)), msg.as_string())
    except Exception as e:
        print(e)
        return 103, f"Error compiling email message\n{e}"


    return 200, "Email Successfully Created!"
    
    #return 200, "Email Successfully Created!"

def isValidEmail(email):
    pattern = '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
    if(re.search(pattern, email)):
        return True
    else:
        return False    

def email_string_checks(email_list):
    if email_list is None:
        return 101, f"No Emails Supplied {email_list}"
    for email_address in email_list:
        if not isValidEmail(email_address):
            return 102, f"Invalid Email String Format {email_address}"


