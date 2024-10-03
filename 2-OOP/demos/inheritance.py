class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)
        return self.salary


class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name} ... ")
        print("Testing is done")

class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
    
    def increase_salary(self, percent, bonus=0):
        self.salary = (super().increase_salary(percent) + bonus)
    
    def __str__(self):
        return ( f"Name: {self.name}\nAge: {self.age}\n" + 
        f"Salary: {self.salary}\nFramework: {self.framework}")

emp1 = Tester('Kev', 22, 72561)
print(emp1.salary)

emp1.increase_salary(20)
print(emp1.salary)

emp1.run_tests()

emp2 = Developer('John', 25, 100000, 'PERN')
emp2.increase_salary(10, 2000)
print(emp2)