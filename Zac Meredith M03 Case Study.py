class Vehicle:
    def __init__(self, type):
        self.type = type
type = input('Enter what type of vehicle this is. Example: car, truck, etc. ')
year = str(input('Enter what year this vehicle was made Example: 2013. '))
make = input('Enter who made this truck Example: Ford, Chevy, Dodge. ')
model = input('Enter what the model is Example: Suburban, Malibu, etc. ')
doors = str(input('Enter how many doors the vehicle has, 2 or 4. '))
roof = input('Enter weather the vehicle has a solid or sun roof. ')
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year 
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def displayInfo(self):
        print(f'Vehicle type: {self.type}')
        print(f'Year: {self.year}')
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Number of Doors: {self.doors}')
        print(f'Type of roof: {self.roof}')


display  = Automobile(type, year, make, model, doors, roof)
display.displayInfo()