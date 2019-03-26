#!/usr/bin/env python3.7

"""03_Tutorial_class_and_static_methods.py.

Third Program of the Schafer Python OOP Tutorial .

"""
import logging
from platform import python_version
from sys import hexversion
from datetime import datetime as dt
import datetime

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

    @classmethod
    def set_raise_amount(cls, amount):
        """Docstring."""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Docstring."""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # @staticmethod
    # def is_workday(day):
    #     """Docstring."""
    #     if (day.weekday() == 6) or (day.weekday() == 6):
    #         return False
    #     return True

    # @staticmethod
    # def is_workday(day):
    #     """Docstring."""
    #     return day.weekday() != 6 or day.weekday() != 6

    # @staticmethod
    # def is_workday(day):
    #     """Docstring."""
    #     return day.weekday() not in (5, 6)

    # @staticmethod
    # def is_workday(day):
    #     """Docstring."""
    #     return day.weekday() in (0, 1, 2, 3, 4)

    @staticmethod
    def is_workday(day):
        """Docstring."""
        return day.weekday() in range(5)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print("", "-" * 88, "\n")
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n", "-" * 88)

Employee.set_raise_amount(1.05)

print("", "-" * 88, "\n")
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_1.full_name())
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(new_emp_2.email)
print(new_emp_2.pay)
print(new_emp_2.full_name())
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(new_emp_3.email)
print(new_emp_3.pay)
print(new_emp_3.full_name())
print("\n", "-" * 88)

my_date1 = datetime.date(2016, 7, 10)
my_date2 = datetime.date(2016, 7, 11)

print("", "-" * 88, "\n")
print(Employee.is_workday(my_date1))
print(Employee.is_workday(my_date2))
print("\n", "-" * 88)
