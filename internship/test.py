class Avengers:
    a1= " "
    a2= " "
    def Avengers():
        print("The construtor")
    def __init__(self, a1, a2):
        self.a1=a1
        self.a2=a2
Marvel = Avengers("Captian", "iron Man")
print(Marvel.a1)