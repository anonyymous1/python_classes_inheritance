# Class

class Person():
    """This is a class about how Ruben operates his daily life."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.energy = 100

    def __str__(self):
        return "{}, {}, {}, {}".format(self.first_name, self.last_name, self.age, self.energy)

    def code(self):
        self.energy -= 10
        print(f'{self.first_name} is Coding.')

    def workout(self):
        self.energy -= 20
        print(f'{self.first_name} is working out.')

    def eat(self):
        self.energy = 100
        print(f'{self.first_name} energy is back at 100.')

    def bday(self):
        self.age += 1
        print(f'{self.first_name} had a bday')

    def check_energy(self):
        print(self.energy)

ruben = Person('Ruben','Cedeno', 33)

print(ruben)
ruben.code()
ruben.check_energy()
print(ruben.age)
ruben.bday()
print(ruben.age)

