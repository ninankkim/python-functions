class Vehicle:
    #class attributes
    # make: 'Tesla'
    # model: 'Cyber Truck'
    # year:'2022'


    def __init__(self):
        self.make = make
        self.model = model 
        self.year = year

    def print_info(self, make, model, year):
        print('The car make is {}, car model is {}, and the year is {}'. format(self.make, self.model, self.year))

car = Vehicle('Tesla', 'CyberTruck', 2022)
print(car.print_info())