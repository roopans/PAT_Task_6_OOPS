# base class for the vehicle details
class vehicle:
    def __init__(self,model, rental):
        self.model = model
        self.rental = rental
    # rental method for the vehicle
    def get_rental(self):
        return f" model: {self.model}, rental: {self.rental}"
#  child class for car, van and bus inheriting vehicle class
class car(vehicle):
    def __init__(self, model, rental):
        super().__init__(model, rental)


    def get_rental(self):
        base_rental = super().get_rental()
        return f"{base_rental}"

class van(vehicle):
    def __init__(self, model, rental):
        super().__init__(model, rental)


    def get_rental(self):
        base_rental = super().get_rental()
        return f"{base_rental}"

class bus(vehicle):
    def __init__(self, model, rental):
        super().__init__(model, rental)


    def get_rental(self):
        base_rental = super().get_rental()
        return f"{base_rental}"
#  create objects for each class and call the get_rental method
get_car_rental = car(2014,1000)
get_van_rental = van(2018,100)
get_bus_rental = bus(2020,5000)
#  print the rental details of different vehicles
print(get_car_rental.get_rental())
print(get_van_rental.get_rental())
print(get_bus_rental.get_rental())

