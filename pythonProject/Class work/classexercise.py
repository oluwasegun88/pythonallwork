class Human:
    #legs=0
    count=1


    def __init__(self, name=" ", age=0):
        self._age = age
        self._name = name
        #self.legs +=1
        Human.count+=1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def do_nothing():
        return "nothing"

    @staticmethod
    def is_minor(age):
        return age<16


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        print("calling the setter")
        if age < 0:
            raise ValueError("Age can be zero")
        self._age = age

    def set_name(self, name):
        self._name = name

    def get_name(self, name):
        self._name = name

    @age.deleter
    def age(self):
        del self._age


h1 = Human("Hadiza", 25)
#h2 = Human("Tunde",26)
h1.age = 20
print(f"Name: {h1._name}\nAge: {h1.age}")
#print(h1.legs)
print(h1.is_minor(76))