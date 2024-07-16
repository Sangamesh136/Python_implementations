class queue:
    e=-1
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def push(self,items):
        self.items.append(items)
        end+=1
    def pop(self):
        if self.isEmpty():
            print("empty")
        removed = self.items[0]
        for i in range(len(self.items)):
            self.items[i-1]=self.items[i]
    end-=1