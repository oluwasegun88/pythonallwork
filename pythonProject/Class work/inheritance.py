class Human:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def full_name(self):
        return f"{self.last_name} {self.first_name}"


     # def __str__(self):
     #    return f"name={self.last_name} {self.first_name}, age={self.age}, sex={self.sex}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name},{self.last_name},{self.age},{self.sex})"



class Manager(Human):
    def __init__(self, first_name: str, last_name: str, age: int, sex: str, bonus: float):
        self.bonus = bonus
        super().__init__(first_name, last_name, age, sex)

    def full_name(self):
        return f"{self.last_name[0].upper()}.{self.first_name}"
        pass

    def pay_salary(self, salary):
        return salary + self.bonus


class Employee(Human):
    def pay_salary(self, salary):
        return salary
        pass


employee1 = Employee("Hadiza", "Umar", 21, "Female")
manager1 = Manager("Segun", "Olayemi", 25, "Male", 1200)

print(employee1.full_name())
print(employee1)
print(manager1.full_name())

# human_list = [employee1, manager1, Human("Sapien", "Homo", 0, "Unknown")]
# for human in human_list:
#     print(human.full_name())
#     print(human.pay_salary(50_000))

print=(f"{employee1!r}")