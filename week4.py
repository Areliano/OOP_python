class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and i am {self.gender}.")  

person1 = Person("John", 30, "transgender")     

person1.introduce()         # Calling the method using dot operator on


