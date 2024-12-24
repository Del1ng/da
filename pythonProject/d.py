#1.
# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Накладено {amount} до рахунку. Баланс: {self.balance}")
#         else:
#             print("Сума внесення повинна бути позитивною.")
#
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Знято {amount} з рахунку.")
#                 print(f"Баланс: {self.balance}")
#             else:
#                 print("Недостатньо коштів на рахунку для зняття.")
#         else:
#             print("Сума зняття повинна бути позитивною.")
# account = BankAccount(12331, 1000)
# account.deposit(500)
# account.withdraw(300)
# account.withdraw(2000)


#2.
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#
#         return f"{self.year} {self.make} {self.model}"
# car = Car("Toyota", "Camry", 2020)
# print(car.get_info())

#3.
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name  #
#         self.position = position  #
#         self.salary = salary
#
#     def get_salary_info(self):
#         return f"Заробітна плата {self.name}: {self.salary} грн"
# employee = Employee("Іван Іванов", "Менеджер", 25000)
# print(employee.get_salary_info())