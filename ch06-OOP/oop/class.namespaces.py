class Person:
    species = "Human"


print(Person.species)
Person.alive = True
print(Person.alive)  # True

man = Person()
print(man.species)
print(man.alive)  # True

Person.alive = False
print(man.alive)  # False

man.name = "Darth"
man.surname = "Vader"
print(man.name, man.surname)
