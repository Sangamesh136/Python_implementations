class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        self.size=0

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insertFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head= node
        node.prev = None
        self.size+=1
    
    def insertLast(self,value):
        node =Node(value)
        temp = self.head
        while(temp!=None):
            temp = temp.next
        temp.next = node
        node.prev = temp
        node.next = None
        self.size+=1
    
    def insertAt(self,value,index):
        node = Node(value)
        temp = self.head
        for i in range(index):
            temp = temp.next
        node.next = temp.next
        node.prev = temp
        temp.next = node
        self.size+=1
    
    def deleteFirst(self):
        if(self.head == None):
             raise Exception("The list is empty!!")
        # temp = self.head
        # while(temp!=None):
        head = head.next
        head.prev = None
        self.size-=1

    def deleteLast(self):
        if(self.head == None):
            raise Exception("The list is Empty!!")
        temp = self.head
        while(temp!=None):
            temp= temp.next
        temp.prev.next = None
        self.size-=1

    def deleteAt(self,index):
        if(index==0):
            self.deleteFirst()
        if(index==self.size):
            self.deleteLast()
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.next=temp.next.next
        temp.next.prev = temp

    def reverse(self):
        temp = self.head
        last = None
        while(temp!=None):
            last = temp
            temp = temp.next
        while(last!=None):
            print(last.value, end="<->")
            last = last.prev
    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.value, end="<->")
            temp= temp.next
        print("None");

DLL = DoubleLinkedList()
DLL.insertFirst(0)
DLL.insertFirst(1)
DLL.insertFirst(2)
DLL.insertFirst(3)
DLL.insertFirst(4)
DLL.display()
DLL.insertAt(2,2)
DLL.deleteAt(2)
DLL.display()
DLL.reverse()