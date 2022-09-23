class Human:
    def __init__(self, name=" ", age=0):
        self._name = name
        self.age = age

    # name = "Hadiza"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        print("calling the setter")
        if name.islower():
            raise ValueError("Name cannot be all lower case")
        self._name = name

        def name(self):
            print("deleting...")
            del self._name


        @name.deleter
        def name(self):
            print("deleting...")
            del self._name


        # return self._name

    # def set_name(self, name):
    #     self._name = name
    #
    # def get_name(self, name):
    #     self._name = name


h1 = Human("Hadiza", 25)
# print(h1.get_name())
# print(h1.name)
# print(h1.__dict__)
# print(h1._Human__name)
# h1.set_name("Racheal")
h1.name = "Racheal"
print(h1.name)
# print(h1.get_name())
# print()
del h1.name
print(h1.name)
