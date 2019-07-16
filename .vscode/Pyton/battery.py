import electricCar

class Battery():
    def __init__(self,battery_size):
        self.battery_size =battery_size

    def get_descriptive_battery(self):
        return 'this is a nice battery' + '--' +str(self.battery_size)

electricar = electricCar.ElectricCar('shanghai','dazhong',2010)
electricar.get_descriptive_name()
