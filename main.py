class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name is {self.name} and age is {self.age}.")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(f"Student name is {self.name}, age is {self.age} and grade is {self.grade}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Teacher's name is {self.name}, age is {self.age} and subject is {self.subject}")


student1 = Student("John Smith", 10, 5.6)
teacher1 = Teacher("Alex Smith", 20, "Math")


my_list = [student1, teacher1]
for i in my_list:
    i.introduce()