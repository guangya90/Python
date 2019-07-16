class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + '-' + self.make + '-' + self.model
        print(long_name)

    def get_odometer(self):
        print('this car meter is'  +'-'+ str(self.odemeter_reading))

    def update_odometer(self,mailes):
        self.odemeter_reading += mailes 


# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         #self.battery = Battery(11)

#     # def get_battery_size(self):
#     #     print(str(self.battery.battery_size))

#     def get_odometer(self):
#         self.odemeter_reading = 20

# electricCar = ElectricCar('12','12','12')
# electricCar.get_descriptive_name()
# electricCar.get_odometer()

# newCar = Car('中国','hongqi',1990)
# newCar.odemeter_reading = 100
# newCar.update_odometer(200)
# newCar.get_descriptive_name()
# newCar.get_odometer()

# # 继承
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         super().__init__(make,model,year)
#         self.battery = battery(11)

#     def get_battery_size(self):
#         print(str(self.battery.battery_size))

#     def get_odometer(self):
#         self.odemeter_reading = 20
            
# electricar = ElectricCar('shanghai','dazhong',2010)
# electricar.get_descriptive_name()
# electricar.get_odometer()
# electricar.get_battery_size()
# electricar.get_odometer()
# print(electricar.odemeter_reading)

# class battery():
#     def __init__(self,battery_size):
#         self.battery_size =battery_size

#     def get_descriptive_battery(self):
#         return 'this is a nice battery' + '--' +str(self.battery_size)

# electricar = ElectricCar('shanghai','dazhong',2010)
# print(electricar.battery.get_descriptive_battery())


