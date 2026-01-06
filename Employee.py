# Base class for the Employee details like name salary and method to calculate salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    #  Salary calculate Method
    def cal_salary(self):
        return f"Name: {self.name}, salary: {self.salary}"
# Child classes for different types of employees inheriting Employee class
class ReqularEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def cal_salary(self):
        return f"Regular Employee - {super().cal_salary()}"

class ContractEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)


    def cal_salary(self):
        return f"Contract Employee - {super().cal_salary()}"

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)


    def cal_salary(self):
        return f"Manager - {super().cal_salary()}"
# create objects of each class and print their salary details
Reqular_Employee = ReqularEmployee("Alice", 50000)
Contract_Employee = ContractEmployee("Bob", 60000)
Manager_Employee = Manager("Charlie", 80000)
#  print salary details foe different types of employees
print(Reqular_Employee.cal_salary())
print(Contract_Employee.cal_salary())
print(Manager_Employee.cal_salary())