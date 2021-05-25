class Vehicle:
    def __init__(self, model):
        self.model = model
        self.meter = 0
    def move(self):
        self.meter += 1
        print(self.meter)



vehicle = Vehicle(2021)
print(vehicle.model)
vehicle.move()
vehicle.move()
vehicle.move()

