class TV():
    def __init__(self):
        self.channel_no =1
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_channel(self, new_channel_no):
        self.channel_no =new_channel_no
        print(f"TV channel: {self.channel_no}")
    def show_status(self):
        if self.is_on == True:
            print(f"TV is on: channel: {self.channel_no}")
        else:
            print("TV is off!")

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()