#!/usr/bin/env python3.7

"""04_Tutorial_inheritance_creating_subclasses.py.

Fourth Program of the Schafer Python OOP Tutorial .

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
logging.basicConfig(filename="LOG_files/LOG_04.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("04_Tutorial_inheritance_creating_subclasses.py RUN / START")

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

    @classmethod
    def set_raise_amount(cls, amount):
        """Docstring."""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Docstring."""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """Docstring."""
        return day.weekday() in range(5)


class Developer(Employee):
    """docstring for Developer."""

    pass


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)


print("", "-" * 88, "\n")
print(dev_1.email)
print(dev_2.email)
print("\n", "-" * 88)
