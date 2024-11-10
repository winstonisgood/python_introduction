class Vehicle: # parent
    def Vehicle_info(self):
        print("This is a vehicle")

class Car(Vehicle): # child
    def Car_info(self):
        print("This is a car")
    
    def Vehicle_info(self):
        print("This is a car override vehicle")

    def Vehicle_info(self, number):
        super().Vehicle_info()
        print("This is a car override vehicle")

# vehicle = Vehicle()
# print(vehicle.Vehicle_info())

car = Car()
car.Car_info()
# car.Vehicle_info()
car.Vehicle_info("this is overload")


def overload():
    print("This is a overload")

def overload(string):
    print("This is a overload" + string)

# overload()
overload("this is overload")