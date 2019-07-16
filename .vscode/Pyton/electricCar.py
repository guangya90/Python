import car
#import battery
# 继承
class ElectricCar(car.Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        #self.battery = Battery(11)

    # def get_battery_size(self):
    #     print(str(self.battery.battery_size))

    def get_odometer(self):
        self.odemeter_reading = 20

newcar = car.Car('zhong','guo',1945)
newcar.get_descriptive_name()

newElec = ElectricCar('12','12',12)
newElec.get_odometer()
print('1212121')
