class Phone():
    def __init__(self, type, ram, time):
        self.type = type
        self.ram = ram
        self.time = time
        self.is_turn_on = True
    def turn_on(self):
        self.is_turn_on = True 
    def turn_off(self):
        self.is_turn_on = False   

phone = Phone("Samsung", 16, 15)

if phone.is_turn_on:
    print(f"Incoming call lasts: {phone.time}")
else:
    print("There is no incoming call.")