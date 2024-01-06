class TV():
    def __init__(self):
        self.volume_lvl = 0
        self.is_on = False

    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False

    def increase_volume(self):
        if self.is_on and 0 <= self.volume_lvl < 10:
            self.volume_lvl += 1
        else:
            print("You can't do that!")
    def decrease_volume(self):
        if self.is_on and 0 < self.volume_lvl <= 10:
            self.volume_lvl -= 1
        else:
            print("You can't do that!")

    def show_status(self):
        if self.is_on == True:
            print(f"Volume level: {self.volume_lvl}")
        else:
            print("TV is off")


tv = TV()
tv.turn_on()
tv.show_status()

for i in range(5):
    tv.increase_volume()

tv.show_status()

for i in range(2):
    tv.decrease_volume()

tv.show_status()
tv.turn_off()