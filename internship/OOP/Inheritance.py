class Human:
    name=""
    age=0
    gender=" "
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender= gender


class student(Human):
    college=" "
    def __init__(self,name,age,gender,college):
        Human.__init__(self,name,age,gender)
        self.college= college

sangamesh =student("Sam",20,"M","BITM")
print(sangamesh.college)