from dataclasses import dataclass
import datetime

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: datetime.date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = datetime.date.today()

        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age >= 18

imran = Person("Imran", datetime.date(2004, 6, 10), "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
print(imran)  # Prints Person(name='Imran', date_of_birth=datetime.date(2004, 6, 10), preferred_operating_system='Ubuntu')

imran2 = Person("Imran", datetime.date(2004, 6, 10), "Ubuntu")
print(imran == imran2)  # Prints True
print(imran.is_adult()) # Prints True 



# ✍️exercise
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

# Re-add the is_adult method to it.