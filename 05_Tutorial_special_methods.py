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


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_employee(dev_2)

print("", "-" * 88, "\n")
print(dev_1.email)
print(dev_2.email)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(dev_1.email)
print(dev_1.prog_lang)
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(mgr_1.full_name())
print(mgr_1.email)
print(mgr_1.pay)
mgr_1.print_employees()
print("\n", "-" * 88)

mgr_1.remove_employee(dev_1)

print("", "-" * 88, "\n")
print(mgr_1.full_name())
print(mgr_1.email)
print(mgr_1.pay)
mgr_1.print_employees()
print("\n", "-" * 88)

print("", "-" * 88, "\n")
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Manager))
print(issubclass(Manager, Developer))
print("\n", "-" * 88)
