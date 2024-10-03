class Employee:
    def __init__(self, name, age, salary):
        self.__dict__['name'] = name
        self.age = age
        #self.set_salary(salary)
        self.salary = salary #properties provide validation
        

    
    def printInfo(self):
        print(self.name, 'is', self.age, 'years old and makes $', self.__salary)
    
    def __str__(self):
        return f"I am printing {self.name}'s info"
    
    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.__salary)})"
    
    def get_salary(self):
        return self.__salary
    
    #property getter
    @property
    def salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        #not pythonic way
        if salary <= 1000:
            raise ValueError('Minimum wage is $1000') #validates salary
        else: 
            self.__salary = salary

    #property setter
    @salary.setter
    def salary(self, salary):
        if salary <= 1000:
            raise ValueError('Minimum wage is $1000') #validates salary
        else: 
            self.__salary = salary

    @property
    def readOnly(self):
        return 'readOnly'
    
    @readOnly.setter
    def readOnly(self, readOnly):
        raise AttributeError('attribute is read only')

e = Employee('kev', 22, 72561)
print (e)
print(e.__dict__)  
e.printInfo()
print(e.__repr__())

try:
    print("Setting salary to $1000")
    e.set_salary(1000)
except:
    print("Can't set salary at or below $1000")

print(e.get_salary())

print("Setting salary to 20000")
e.set_salary(20000)
print(e.get_salary())
print("printing from property", e.salary)

#read only attribute example
print(e.readOnly)

try:
    e.readOnly = "overwrite"
except:
    print("this is attribute doesn't change")
finally:
    print(e.readOnly)