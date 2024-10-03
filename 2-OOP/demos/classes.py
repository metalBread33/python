class Employee:
    def __init__(self, name, age, salary, SSN):
        self.__dict__['name'] = name
        self.age = age
        #self.set_salary(salary)
        self.salary = salary #properties provide validation
        self.__ssn = SSN
        self.__monthly = None

    
    def printInfo(self):
        print(self.name, 'is', self.age, 'years old and makes $', self.__salary)
    
    def __str__(self):
        return f"I am printing {self.name}'s info"
    
    def __repr__(self):
        return f"Employee({repr(self.name)}, {repr(self.age)}, {repr(self.__salary)})"
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        #not pythonic way
        if salary <= 1000:
            raise ValueError('Minimum wage is $1000') #validates salary
        else: 
            self.__salary = salary

    #property getter
    @property
    def salary(self):
        return self.__salary

    #property setter
    @salary.setter
    def salary(self, salary):
        if salary <= 1000:
            raise ValueError('Minimum wage is $1000') #validates salary
        else: 
            self.__salary = salary
            self.__monthly = None

    #read only example
    @property
    def readOnly(self):
        return 'readOnly'
    
    @readOnly.setter
    def readOnly(self, readOnly):
        raise AttributeError('attribute is read only')
    
    #write only example
    @property
    def ssn(self):
        return("Cannot access write only attribute")
    
    @ssn.setter
    def ssn(self, SSN):
        self.__ssn = SSN

    @property
    def monthlySalary(self):
        if self.__monthly is None:
            print("calculating monthly salary")
            self.__monthly = self.__salary / 12
        return self.__monthly


e = Employee('kev', 22, 72561, '0')
print (e)
print(e.__dict__)  
e.printInfo()
print(e.__repr__())
print("employee's monthly salary is:", e.monthlySalary)
print("employee's monthly salary is:", e.monthlySalary)

try:
    print("Setting salary to $1000")
    e.set_salary(1000)
except:
    print("Can't set salary at or below $1000")

print(e.get_salary())

print("Setting salary to 20000")
e.salary = 20000
print(e.get_salary())

print("employee's monthly salary is:", e.monthlySalary)
print("employee's monthly salary is:", e.monthlySalary)

print("printing from property", e.salary)


#read only attribute example
print(e.readOnly)

try:
    e.readOnly = "overwrite"
except:
    print("this is attribute doesn't change")
finally:
    print(e.readOnly)

#write only attribute example
print("Changing ssn")
e.ssn = '000-00-0000'
print("Change completed")
try:
    print(e.ssn)
except:
    print("Cannot print write only attribute")