class Friend():
    def __init__(self):
        self.value = "3 lakh"
        
    def sh(self):
        print(self.value)

class You(Friend):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.value = "Himalayan bike"
        
    def sh(self):
        print(self.value)

fr = Friend()
y = You()
fr.sh()  # Output: 3 lakh
y.sh()   # Output: Himalayan bike