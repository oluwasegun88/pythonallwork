class CustomClass:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __str__(self):
        return self.number

    def __repr__(self):
        return self.number


c1 = CustomClass(6)
c2 = CustomClass(2)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
