import random

class Thermometer():
    def __init__(self):
        self.value = 0.0
        self.is_on = False

    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False

    def measure_temp(self):
        self.measure = random.randint(34.0,42.0)
        print(f"Random number: {self.measure}")
    def display_temp(self):
        print(f"The temperature equals {self.measure}")
        if self.measure >= 37.0:
            print("fever!")
        if self.measure >= 41.0:
            print("CRITICAL TEMPERATURE!!")

therm = Thermometer()
therm.on()
therm.measure_temp()
therm.display_temp()
therm.off()



    