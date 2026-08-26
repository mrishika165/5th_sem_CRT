# class A:
#     a = 10 #public
#     _b = 20#protected
#     __c = 30 #private
# obj = A()
# print(obj.a)
# print(obj._b)
# print(obj._A__c)

#Access snd modifybprivate members from class using methods
# class Bank:
#     def __init__(self,balance): 
#         self.__balance = balance # private
#     def credit(self,amount):
#         self.__balance+=amount
#     def debit(self,amount):
#         self.__balance-=amount
#     def display(self):
#         print("Current balance:", self.__balance)
# b = Bank(1000)
# b.display()
# b.credit(1000)
# b.display()
# b.debit(2500)
# b.display()


