class Car:

    def __init__(self, colour, b, age):
        self.colour = colour
        self.fuel = 10
        self.condition = b * 2
        self.eco_mode = False
        self.fuel_consumption = 14
        self.production_year = 2023 - age


    def milage_range(self):
        milage_range = self.fuel / self.fuel_consumption * 100 * 0.9 # 0.9, żeby zaniżyć
        return round(milage_range)

    def set_mode(self, mode):
        if mode == 'eco':
            self.fuel_consumption = 10
            self.eco_mode = True
        elif mode == 'standard':
            self.fuel_consumption = 14
            self.eco_mode = False
        else:
            print('No change')

car1 = Car('red', 2, 2) #obiekt klasy Car
car2 = Car('white', 4, 10)
neighbour_car = Car('black', 1, 3)
print(car1.colour)
car1.colour = 'blue'
print(car1.colour)
#if car2.fuel > 5:
#neighbour_car.condition +=1

print(neighbour_car.milage_range())

car2.set_mode('standard')
print(car2.fuel_consumption)
