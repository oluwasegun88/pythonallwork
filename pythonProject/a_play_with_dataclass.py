from dataclasses import dataclass, field, fields, make_dataclass


class Person:
    pass

    # class Person:
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age

    def empty_list(self):
        return []


    @dataclass(order=True)
    class Person:
       # __slots__ = ['name','age']
        sort_with: tuple = field(init=False, repr=False,)
        name: str
        age: int
        height: int = field(default=0)
        children: list = field(default_factory=lambda:[])

        def __post_init__(self):
            self.sort_with = (self.height, self.age)

        def get_age(self):
            return self.age()

    p1 = Person("Hadiza", 21)
    p2 = Person("Victor", 21)

    #p1.name = "Banke"

    p1.hello = "my_life"

    print(p1.hello)
    print(p1.__dict__)
    # print(p1.get_age())
    # print(p1 < p2)
    print(fields(p1))


    Human = make_dataclass("Human", ["name","age"])
    h1 = Human("Hadiza",23)

    print(h1)

    class Animal:
        __slots__ = ['legs']

    def __init__(self,legs):
        self.legs = legs

    anime = Animal(4)
    print(anime.legs)
    anime.legs = 8