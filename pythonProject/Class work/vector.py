import math


class Vector:
    def __init__(self,x: float, y: float) -> None:
        self.x=x
        self.y=y


    def __abs__(self):
        return math.hypot(self.x, self.y)


    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)

    def __str__(self):
        return f"{self.x}i + {self.y}j"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return 0

    def __lt__(self, other):
        return abs(self) < abs(other)


    def __bool__(self):
        return True

V1= Vector(2,4)
V2=Vector(1,6)
V3=V1 + V2


print(bool(V1))
print(V1)
print(V3)
lst=[V3,V1,V2]
print(lst)
lst.sort()
print(lst)

