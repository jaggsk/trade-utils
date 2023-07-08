from setuptools import setup, find_packages
import os
import sys
import re
import shutil


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def read_all(f):
    with open(f) as I:
        return I.read()

requirements = map(str.strip, open("requirements.txt").readlines())
#print(requirements)
version = get_version('tradeutil')

#print(read_all('README.md'))

setup(name='trade-utils',
      version=version,
      description="Suite of scripts to assist financial analysis/trading",
      long_description=read_all("README.md"),
      classifiers=[
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License',
            #'Intended Audience :: Developers',
            #'Intended Audience :: Financial and Insurance Industry',
            'Operating System :: OS Independent',
            'Development Status :: 3 - Alpha',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.11',
      ],  # Get from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Trading Utilities',
      author='Kevin Jaggs',
      author_email='kevin.jaggs@gmail.com',
      url='https://github.com/jaggsk/trade-utils',
      license='MIT',
      packages=['tradeutil'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
