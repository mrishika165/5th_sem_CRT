#Polymorphism - having many forms
# print(10+20)
# print("abc" + "xcv")
#here + operator is same but its behaviour is different 

'''
Compile-time:
    1.Function overloading -multiple functions with same name but diff argument list
    2.Operator overloading - 
Run-time:
    1.Method overriding - same method in both parent and child class
'''
#Function overloading
# def add(a,b):
#     return a+b 
# def add(a,b,c):
#     return a+b+c 
# def add(a,b,c,d):
#     return a+b+c+d
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))
'''
python doesnot support function overloading directly 
we can achieve this using variable-length arguments(using *)
'''
# def add(*values):
#     return sum(values)
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))


'''
Operator overloading
'''
# class A:
#     def __init__(self,x):
#         self.x = x 
#     def __add__(self,val):
#         return self.x + val.x
#     def __sub__(self, val):
#         return self.x - val.x
#     def __lt__(self,val):
#         return self.x < val.x
# a = A(10)
# b = A(20)
# print(a+b)
# print(a-b)
# print(a<b)


#Example 
# class B:
#     def __init__(self,x,y):
#         self.x =x 
#         self.y = y
#     def __add__(self,val):
#         return (self.x + val.x , self.y + val.y)

#     def __sub__(self,val):
#         return (self.x - val.x , self.y - val.y)
# a = B(10,20)
# b = B(30,40)
# print(a+b)
# print(a-b)


'''
method overriding
'''
# class Parent:
#     def display(self):
#         print("Parent class diaplay method")
# class Child(Parent):
#     def display(self):
#             print("Child class diaplay method")
# c = Child()
# c.display()
# Parent.display(c) # parent class method using child class object
# Child.display(c)
# p = Parent()
# p.display()
# Child.display(p)

'''
Duck typing
'''
class Dog:
    def Sounds(self):
        print("Bark")
class Cat:
    def Sounds(self):
        print("Meow")
def make_sound(animal):
    animal.Sounds()
d = Dog()
make_sound(d)
c = Cat()
make_sound(c)