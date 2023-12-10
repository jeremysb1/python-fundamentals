import pickle
from dataclasses import dataclass
@dataclass
class Person:
    first_name: str
    last_name: str
    id: int
    def greet(self):
        print(f'Hi, I am {self.first_name} {self.last_name}'
              f' and my ID is {self.id}')

people = [
    Person('Donnie', 'Brasco', 123),
    Person('Johhny', 'Keys', 456),
]

with open('data.pickle', 'wb') as stream:
    pickle.dump(people, stream)

for person in people:
    person.greet()