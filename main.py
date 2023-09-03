"""
Mostly going to use this script to test IDE features
"""
from typing import Iterable

# Type Hints

# Primitives
age: int = 20
name: str = "John"
is_employed: bool = True

# Sequences
companies: list[str] = ["TCS", "IBM", "Barclays"]
cgpas: tuple[float | None, ...] = (80.0, None, 8.5)

# Iterable
address: dict[str, int | str] = {
    "flat": 207,
    "tower": "A",
    "street": "Gandhi Marg Road",
    "city": "Bhubaneswar",
    "state": "Odisha",
    "pin": 759145,
}


def display_items(items: Iterable) -> None:
    """
    This is a generic function that takes an Iterable and displays in the console
    """
    for company in items:
        print(company, end=", ")


def display_address(my_address: dict[str, int | str]) -> None:
    """
    Takes an address of dict and displays in a table.
    """
    for key, value in my_address.items():
        print(f"{key:<20} {value}")


if __name__ == "__main__":
    display_items(companies)
    print("")
    display_items(cgpas)
    print("")
    display_address(address)
