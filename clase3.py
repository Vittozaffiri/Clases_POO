from hashlib import new
from tkinter import N


class Student:

    def __init__(self, name, family_name, age):

        self.first_name = name    
        self.last_name = family_name
        self.age = age

    def greet(self):

        #return "Hello my name is" + self.first_name
        return f"hello, my name is {self.first_name}"


class course: 

    def __init__(self, name):

        self.name = name
        self.students = []

    def add_student(self,student):

        self.students.append(student)

    #def remove_student(self, student):
        

    def list_students(self):
        for student in self.students:
            print(student.greet())


my_course = course("POO")
new_student = Student("Andres", "Howard", 45)
other_student = Student("Vicente", "cuevas", 20)

my_course.add_student(new_student)
my_course.add_student(other_student)


            

new_student = Student("Andres", "Howard", 45)

print(new_student.greet())

