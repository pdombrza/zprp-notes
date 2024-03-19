# Employee

# emp_id
# name
# gender
# salary
# age
# list of users who viewed this employee's record

## include in hash:
# emp_id
# name
# gender

## limit the fields used in comparisons

## metadata about the currency of the salary

from dataclasses import dataclass, field
from dataclasses import fields
from datetime import datetime
from pprint import pprint

@dataclass(order=True, unsafe_hash=True)
class Employee:
    emp_id: int = field()
    name: str = field()
    gender: str = field()
    salary: int = field(hash=False, repr=False, metadata={"units": "BTC"})
    age: int = field(hash=False)
    viewed_by: list = field(default_factory=list, compare=False, repr=False)

    def access(self, viewer_id):
        self.viewed_by.append({viewer_id, datetime.now()})


e1 = Employee(emp_id=784318, name="Janusz Strzała", gender="male", salary=20, age=36)
e2 = Employee(emp_id=784329, name="Halina Strzała", gender="female", salary=11, age=25)
