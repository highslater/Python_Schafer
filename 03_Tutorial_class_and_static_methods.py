#!/usr/bin/env python3.7

"""03_Tutorial_class_and_static_methods.py.

Third Program of the Schafer Python OOP Tutorial .

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
logging.basicConfig(filename="LOG_files/LOG_03.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("03_Tutorial_class_and_static_methods.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


class Employee():
    """docstring for Employee."""

    # class variables.
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        """Docstring."""
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_employees += 1

    def full_name(self):
        """Docstring."""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Docstring."""
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("", "-" * 88, "\n")
print("", emp_1.email)
print("", emp_2.email)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print("", emp_1.full_name())
print("", emp_2.full_name())
print("\n", "-" * 88)

'''
# print("", Employee.email(emp_1))

    Traceback (most recent call last):
    File "./02_Tutorial_Classes_variables.py", line 60, in <module>
        print("", Employee.email(emp_1))
    AttributeError: type object 'Employee' has no attribute 'email'
'''

print("", "-" * 88, "\n")
print("", Employee.full_name(emp_1))
print("", Employee.full_name(emp_2))
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(Employee.raise_amount)
print("", emp_1.pay)
emp_1.apply_raise()
print("", emp_1.pay)
print(emp_1.raise_amount)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print("", emp_1.__dict__)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print("", Employee.__dict__)
print("\n", "-" * 88)

Employee.raise_amount = 1.05

print("", "-" * 88, "\n")
print(Employee.raise_amount)
print("", emp_1.pay)
emp_1.apply_raise()
print("", emp_1.pay)
print(emp_1.raise_amount)
print("\n", "-" * 88)

Employee.raise_amount = 1.04
emp_1.raise_amount = 1.05

print("", "-" * 88, "\n")
print(Employee.raise_amount)
print("", emp_1.pay)
emp_1.apply_raise()
print("", emp_1.pay)
print(emp_1.raise_amount)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(" Number of employees:", Employee.number_of_employees)
print("\n", "-" * 88)
