print("name - VIDHI SHARMA  roll no - 1900300100242")
class student:
    def __init__(self, name, roll):
        self.n= name
        self.r= roll
    def setAge(self, age):
        self.a=age
    def setMarks(self, marks):
        self.m=marks
    def Display(self):
        print("Name of the student =", self.n)
        print("Roll number of the student =", self.r)
        print("Age of the student =", self.a)
        print("Marks of the student =", self.m)

    pass

sname=input("Enter name = ")
sroll=int(input("Enter roll number = "))
s=student(sname, sroll)
age=int(input("Enter age = "))
s.setAge(age)
marks=int(input("Enter marks = "))
s.setMarks(marks)
s.Display()