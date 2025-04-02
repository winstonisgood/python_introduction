class employee:
    def __init__(self, name, age, salary):
        self._name = name
        self.age = age
        self.__salary = salary

    def get_name(self):
        return self._name

    # def set_name(self, name):
    #     self.__name = name;


class research_employee(employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self._name = name
        self.__salary = salary

    def print(self):
        print(self.age)
        print(self._name)
        self._name = 'jim'
        print(self._name)
        # print(self.__salary)


research_employee = research_employee('jack', 24, 86000)
research_employee.print()
print(research_employee.__dict__)
print(research_employee._name)
# print(research_employee.__salary)

# instance
jim = employee('jim', 23, 85000)
#
# # print("Employee name", jim.name)
#
print(jim.__dict__)
# # jim.set_name('jame')
# # jim._name = 'jame'
# print(jim.__dict__)


# print(jim.__name)
# print("Employee age", jim.age)
# print("Employee salary", jim.salary)