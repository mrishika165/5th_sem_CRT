#Inheritance acquiring properties from one class to other
#single inheritance 
# class A:
#     def display(self):
#         print("This is class A display method")
# class B(A):
#     def display2(self):
#         print("this is class B display method")
# b = B()
# a = A()
# a.display()
# b.display()
# b.display2()


#Multilevel Inheritance 
# class A:
#     def display(self):
#         print("class A display")
# class B(A):
#     def display1(self):
#         print("hoi hoiii")
# class C(B):
#     def display2(self):
#         print("xcvgbhnj")
# c = C()
# c.display()
# c.display2()


#Multiple 
class A:
    def display(self):
        print("class A display")
class B:
    def display1(self):
        print("hoi hoiii")
class C(B,A):
    def display2(self):
        print("xcvgbhnj")
c = C()
c.display()

