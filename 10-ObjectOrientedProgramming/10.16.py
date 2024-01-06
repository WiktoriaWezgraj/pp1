class Phone():
    def __init__(self, model, ram, color):
        self.model = model
        self.ram = ram
        self.color=color
        self.is_on = True
        self.is_calling = False
    def call(self):
        self.is_calling = True 
    def turn_off(self):
        self.is_on = False   

phone = Phone("Samsung", 16, "pink")
print(f"My phone is {phone.model} ",end="")
print(f"It has {phone.ram} GB RAM. ",end="")
print(f"It's {phone.color}.")