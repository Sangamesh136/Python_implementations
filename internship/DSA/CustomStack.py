class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==-1
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print("UNDERFLOW")
    def display(self):
        print(self.items)
    def rev(self):
        print("[",end=" ")
        for i in range(len(self.items)):
            print(self.items[len(self.items)-i-1], ",",end=" ")
        print("]")
    def printEven(self):
        print("[", end="")
        for i in range(len(self.items)):
            if(self.items[i]&  1)==0:
                print(self.items[i]," ,", end=" ")
        print("]")
    def sort(self):
        for i in range(len(self.items)-1):
            for j in range(len(self.items)-i-1):
                if self.items[j]>self.items[j+1]:
                    # self.items[j],self.items[j+1]=self.items[j+1],self.items[j]
                    temp=self.items[j]
                    self.items[j]=self.items[j+1]
                    self.items[j+1]=temp
        self.display()

s=Stack()
s.push(0)
s.push(4)
s.push(2)
s.push(45)
s.push(10)
s.display()
# s.rev()
# s.printEven()
s.sort()