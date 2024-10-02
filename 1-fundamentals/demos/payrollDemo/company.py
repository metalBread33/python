from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('---------------------')

    def pay_employees(self):
        print('Paying Employees')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('-----------------')

def main():
    my_company = Company()

    employee = Employee('Kevin', 'Foughty', 72561)
    my_company.add_employee(employee)

    my_company.display()
    my_company.pay_employees()

main()