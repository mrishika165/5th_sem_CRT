# class Example:
#     x = 100
#     def display(self):
#         print("Hii")
# obj = Example()
# obj.display()
# print(obj.x)


# from math import pi
# class Circle:
#     r = 10
#     def area(self):
#         return pi * self.r * self.r
#     def perimeter(self):
#         return 2*pi*self.r
# obj = Circle()
# print(obj.area())
# print(obj.perimeter())



# class Student:
#     def __init__(self):
#         print("hii")
# Bob = Student()

#parameterized constructor
# class Student:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name     
# s1 = Student(12,"Rishi")
# print(s1.name)



class Bank:
    def __init__(self,balance):
        self.balance = balance 
    def credit(self,amount):
        self.balance += amount
        print(self.balance)
    def debit(self,amount):
        self.balance -= amount 
        print(self.balance)

b1 = Bank(5000)
# b1.credit(2000)
# b1.debit(700)
while True:
    print("1.Credit\n2.Debit\n3.Exit")
    choices = int(input())
    if choices == 1:
        amount = int(input())
        b1.credit(amount)
    elif choices == 2:
        amount = int(input())
        b1.debit(amount)
    elif choices == 3:
        break
