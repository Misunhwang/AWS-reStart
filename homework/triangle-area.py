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

        try:
            assert a+b > c
            assert b+c > a
            assert c+a > b
        except Exception as e:
            print(f"-- Error happen : {e}")
        else:
            print("-- Valid")

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

print("\nTriangle(1,2,5)")
trangle = Triangle(1,2,5)
print("Area : ", trangle.area())

"""
<Expect results>

Triangle(3,4,5)
-- Valid
Area :  6.0

Triangle(8,9,5)
-- Valid
Area  :  19.9

Triangle(6,3,7)
-- Valid
Area  :  8.94

Triangle(1,2,5)
-- Error happen : 
"""