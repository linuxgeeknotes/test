class Person:

    count = 0
    def __init__(self, name : str, age : int, height : int):
        self.name = name
        self.age = age
        self.height = height
        Person.count+=1

    def getolder(years):
        self.age+=years
person1 = Person('Vishnu', 40, 168)
person2: Person = Person("Adriana", 30, 164)

print(person1.name)
print(person1.age)
print(person1.height)



print(person2)
print(person2.age)
print(person2.height)

print(Person.count)