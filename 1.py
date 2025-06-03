import getpass
class Person:

        def __init__(self, name : str, age : int, height : int):
                self.name = name
                self.age = age
                self.height = height

person1 = Person('Vishnu', 40, 168)
person2 = Person('Adriana', 30, 164)

print(person2.name)
print(person2.age)
print(person2.height)
print(person1.name)
print(person1.age)
print(person1.height)





pswd = getpass.getpass('Password:')


