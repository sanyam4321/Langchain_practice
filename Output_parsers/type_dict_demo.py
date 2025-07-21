from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': '1', 'age': 50}
print(new_person)