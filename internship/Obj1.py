class Student:
    name = ""
    age = 0
    USN = 0
    gender= 0
    def __init__(self,name,age,USN,gender):
        self.name=name
        self.age = age
        self.USN= USN
        self.gender = gender

Sam = Student("sam","20","40","male")
print(Sam.age)

