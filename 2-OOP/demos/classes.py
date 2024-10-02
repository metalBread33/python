class Employee:
    def __init__(self, name, age):
        self.__dict__['name'] = name
        self.age = age
    
    def printInfo(self):
        print(self.name, 'is', self.age, 'years old')
    
    def __str__(self):
        return f"I am printing {self.name}'s info"
    
    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)})"

e = Employee('kev', 22)
print (e)
print(e.__dict__)  
e.printInfo()
print(e.__repr__())