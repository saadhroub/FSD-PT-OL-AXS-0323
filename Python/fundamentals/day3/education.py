############################################################
# This example illustrates the concepts of objects and     #
# classes in python and introduced the OOP inheritance     #
# princicple, it contains Person, Student, Eployee classes #
############################################################

class Person:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.date_of_birth = dob
    
    def details(self):
        print(f"Name: {self.name}, \nID: {self.id}\nDate of Birth {self.date_of_birth} ")
    
    def greeting(self,Person):
        print("I am person")


class Employee(Person):
    def __init__(self, name, id, dob,position, salary):
        super().__init__(name, id, dob)
        self.position = position
        self.salary = salary

    def details(self):
        super().details()
        print(f"Salary: {self.salary}\nPosition: {self.position}")

    def greeting(self,Person):
        print("I am Employee")


class Teacher(Employee):
    def __init__(self, name, id, dob,position, salary, courses =[]):
        super().__init__(name, id, dob,position, salary)
        self.courses=courses
    
    def details(self):
        super().details()
        print(f"My Courses: {self.courses}")
    
    def greeting(self,Person):
        print("I am Teacher")


p1 = Person("Saad Hroub", 1234567654, '12/12/1980')
e1 = Employee("Azzam Ahmadr", 1234567654, '12/12/1980', "Developer", 3000)
t1 = Teacher("Khalid Khader", 1234567654, '12/12/1980', "Instructor", 5000, ["Python", "Java"])
    







