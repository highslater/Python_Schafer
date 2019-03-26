#!/usr/bin/env python3.7

"""01_Tutorial_Classes_and_Instances.py.

First Program of the Schafer Python OOP Tutorial .

"""
import logging
from platform import python_version
from sys import hexversion
from datetime import datetime as dt

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_01.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("01_Tutorial_Classes_and_Instances.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


class Employee():
    """docstring for Employee."""

    def __init__(self, first, last, pay):
        """Docstring."""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        """Docstring."""
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("", "*" * 88, "\n")
print("", emp_1.email)
print("", emp_2.email)
print("\n", "*" * 88)

print("", "*" * 88, "\n")
print("", emp_1.full_name())
print("", emp_2.full_name())
print("\n", "*" * 88)

print("", "*" * 88, "\n")
print("", Employee.full_name(emp_1))
print("", Employee.full_name(emp_2))
print("\n", "*" * 88)
