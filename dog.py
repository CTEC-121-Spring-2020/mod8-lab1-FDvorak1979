class Dog:
    def __init__(self, name):
        self._name = name

    def setNAme(self, name):
        self.name = name
    
    def getNAme(self):
        return self._name
    
    def bark(self):
        print("bark! bark! bark!")

        
