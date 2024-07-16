class base:
    def __init__(self):
        self.a = 1000

class derived(base):
    def __init__(self):
        base.__init__(self)
        print("Protected element")
        print(self.a)
ob2 = base()
ob3 = derived()
print(ob2.a)
print(ob3.a)