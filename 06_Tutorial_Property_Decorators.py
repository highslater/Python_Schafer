#!/usr/bin/env python3.7

"""06_Tutorial_Property_Decorators.py.

Sixth Program of the Schafer Python OOP Tutorial .

"""
import logging
from platform import python_version
from sys import hexversion
from datetime import datetime as dt
# import datetime

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_06.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("06_Tutorial_Property_Decorators.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


class Employee():
    """docstring for Employee."""

    def __init__(self, first, last):
        """Docstring."""
        self.first = first
        self.last = last

    @property
    def email(self):
        """Docstring."""
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def full_name(self):
        """Docstring."""
        return '{} {}'.format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        """Docstring."""
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        """Docstring."""
        print(" Delete Name!\n")
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

print('', "-" * 88, '\n')
print('', emp_1.first)
print('', emp_1.last)
print('', emp_1.email)
print('', emp_1.full_name)
print('\n', "-" * 88, '\n')

emp_1.first = 'Jim'

print('', "-" * 88, '\n')
print('', emp_1.first)
print('', emp_1.last)
print('', emp_1.email)
print('', emp_1.full_name)
print('\n', "-" * 88, '\n')

emp_1 = Employee('John', 'Smith')

print('', "-" * 88, '\n')
print('', emp_1.first)
print('', emp_1.last)
print('', emp_1.email)
print('', emp_1.full_name)
print('\n', "-" * 88, '\n')

emp_1.full_name = 'Corey Schafer'

print('', "-" * 88, '\n')
print('', emp_1.first)
print('', emp_1.last)
print('', emp_1.email)
print('', emp_1.full_name)
print('\n', "-" * 88, '\n')

del emp_1.full_name

print('', "-" * 88, '\n')
print('', emp_1.first)
print('', emp_1.last)
print('', emp_1.email)
print('', emp_1.full_name)
print('\n', "-" * 88, '\n')
