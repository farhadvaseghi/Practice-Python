class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self, other):
        return f"Hello {other}, my name is {self.name}"
