class Triangle:
    def __init__(self):
        self.a = float(input("Enter length of side a:"))
        self.b = float(input("Enter length of side b:"))
        self.c = float(input("Enter length of side c:"))

class Area(Triangle):
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = (s * (s - self.a)*(s - self.b)*(s - self.c)) ** 0.5
        print("Area of triangle is {} square cm".format(area))

t =Area()
t.area()