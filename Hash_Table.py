class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.values = [None] * size

    def add(self, key, value):
        index = hashing_func(key, self.size)

        self.values[index] = value

    def get(self, key):
        index = hashing_func(key, self.size)
        return self.values[index]

    def print(self):
        for i in self.values:
            if i:
                print(i.age, i.last_name, i.mobile)

    
class Person:
    def __init__(self, age, last_name, mobile):
        self.age = age
        self.last_name = last_name
        self.mobile = mobile


def hashing_func(value, size):
    number = 0
    for i in str(value):
        number += ord(i)
    index = number % size

    return index


ht = Hash_Table(100)

ht.add("michal", Person(17, "Pavlicek", "773543802"))
ht.add("Michal", Person(18, "Pavlicek", "773543802"))
ht.add("lukas", Person(17, "Prochy", "608456789"))
ht.add("vojcek", Person(16, "Olsr", "777489456"))
ht.add(1, Person(16, "Shit", "777489456"))

ht.print()