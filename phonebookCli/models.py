from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    phone_number: str
    info: str

    def __repr__(self):
        return f"{self.last_name}, {self.first_name}, {self.phone_number}, {self.info}"
