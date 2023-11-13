# Week2 Homework6
import math

class Shape:
    def area():
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        assert a+b > c
        assert b+c > a # AssertionError for Triangle(5,2,1)
        assert c+a > b

    def area(self):
        semi = (self.a + self.b + self.c)/2
        area = semi * (semi-self.a) * (semi-self.b) * (semi-self.c)
        return round(math.sqrt(area),2)
    
print("Triangle(3,4,5)")
trangle = Triangle(3,4,5)
print("Area : ", trangle.area())

print("\nTriangle(8,9,5)")
trangle = Triangle(8,9,5)
print("Area  : ", trangle.area())

print("\nTriangle(6,3,7)")
trangle = Triangle(6,3,7)
print("Area  : ", trangle.area())

print("\nTriangle(5,2,1)")
trangle = Triangle(5,2,1) # AssertionError 
print("Area : ", trangle.area())


"""
<Expect results>

Triangle(3,4,5)
Area :  6.0

Triangle(8,9,5)
Area  :  19.9

Triangle(6,3,7)
Area  :  8.94

Triangle(5,2,1)
"""