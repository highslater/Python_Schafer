#!/usr/bin/env python3.7

"""05_Tutorial_special_methods.py.

Fifth Program of the Schafer Python OOP Tutorial .

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
logging.basicConfig(filename="LOG_files/LOG_05.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("05_Tutorial_special_methods.py RUN / START")

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

    def __repr__(self):
        """Docstring."""
        return "Employee('{}', '{}', '{}')".format(
            self.first, self.last, self.pay)

    def __str__(self):
        """Docstring."""
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        """Docstring."""
        return self.pay + other.pay

    def __len__(self):
        """Docstring."""
        return len(self.full_name())

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
    """Docstring for Developer."""

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        """Docstring."""
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    """Docstring for Manager."""

    def __init__(self, first, last, pay, employees=None):
        """Docstring."""
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        """Docstring."""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        """Docstring."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        """Docstring."""
        for emp in self.employees:
            print('-->', emp.full_name())


emp_1 = Developer('Corey', 'Schafer', 50000, 'Python')
emp_2 = Developer('Test', 'Employee', 60000, 'Java')

print('', "-" * 88, "\n")
print('', emp_1)
print('\n', "-" * 88, "\n")

print('', "-" * 88, "\n")
print('', repr(emp_1))
print('\n', "-" * 88, "\n")

print('', "-" * 88, "\n")
print('', emp_1.__str__())
print('\n', "-" * 88, "\n")

print('', "-" * 88, "\n")
print('', emp_1.__repr__())
print('\n', "-" * 88, "\n")

print('', "-" * 88, "\n")
print(emp_1 + emp_2)
print('\n', "-" * 88, "\n")

print('', "-" * 88, "\n")
print(len('four'))
print('four'.__len__())
print('\n', "-" * 88, "\n")

print('', "-" * 88, "\n")
print(len(emp_1))
print(len(emp_2))
print('\n', "-" * 88, "\n")
