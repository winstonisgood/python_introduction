class student:
    __school_name = "ABC School"
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_school_name(self):
        return self.__school_name

    def get_name(self, string):
        return self.get_name() + string
    
#     def __str__():
#         return "string"

# def __str__():
#         return "string"
# print(__str__())
# print(student.__str__())

# winston = student("Winston", 12, 6)
# print(winston)
# print(winston.school_name)
# student.school_name = "CDE School"

# student.get_name()
# student.get_name("_c")
# james = student("James", 13, 7)
# print(james)
# print(james.school_name)
# print(james.name)

# winston._name = "James"
# print(winston)
# print(winston.school_name)
# print(winston._name)