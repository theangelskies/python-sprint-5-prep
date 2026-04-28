from dataclasses import dataclass
from enum import Enum
from typing import List
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]
print("Welcome to Laptop Library!")
print(f"Available operating systems: {', '.join(os.value for os in OperatingSystem)}")

def parse_operating_system(user_input: str) -> OperatingSystem:
    for operating_system in OperatingSystem:
        if user_input.lower() == operating_system.value.lower():
            return operating_system
    print("Invalid operating system", file=sys.stderr)
    sys.exit(1)

name = input("Enter name: ")

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Age must be a number", file=sys.stderr)
    sys.exit(1)

operating_system_input = input("Enter preferred operating system: ")
preferred_operating_system = parse_operating_system(operating_system_input)

person = Person(name=name, age=age, preferred_operating_system=preferred_operating_system)

possible_laptops = find_possible_laptops(laptops, person)
print(f"We have {len(possible_laptops)} laptops for your preferred operating system")

operating_system_counts = {}
for laptop in laptops:
    if laptop.operating_system in operating_system_counts:
        operating_system_counts[laptop.operating_system] += 1
    else:
        operating_system_counts[laptop.operating_system] = 1

best_operating_system = max(operating_system_counts, key=operating_system_counts.get)

if best_operating_system != preferred_operating_system:
    print(f"If you choose {best_operating_system.value}, more laptops are available")

#     ✍️exercise
# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.