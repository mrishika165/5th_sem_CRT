# class Example:
#     x = 100
#     def display(self):
#         print("Hii")
# obj = Example()
# obj.display()
# print(obj.x)


from math import pi
class Circle:
    r = 10
    def area(self):
        return pi * self.r * self.r
    def perimeter(self):
        return 2*pi*self.r
obj = Circle()
print(obj.area())
print(obj.perimeter())