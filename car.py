class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer = 0 #對類別新增一個預設值
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name
    def read_odometer(self):#試著印出odometer
        print(f"車子里程{self.odometer}")
    def update_odometer(self,mileage):#用方法來修改odometer
        if self.odometer > mileage:#加入條件式
            print("你不能將里程調小")
        else:
            self.odometer=mileage
    def increase_odometer(self,miles):#用方法做加總
        self.odometer+=miles
    def fill_gas_tank(self): #複寫父類別的方法
        print("fill gas for my car")

class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) 
        self.battery=Battery()#在類別中引入剛剛的Battery類別
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"電池尺寸{self.battery_size}")
    def get_range(self):#再加入判斷式
        if self.battery_size==100:
            range=315
        elif self.battery_size==75:
            range=260
        print(f"這個電池可續航{range}公里")    