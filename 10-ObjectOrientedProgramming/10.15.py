class TV():
    def __init__(self):
        self.channels = []
        self.channel = 0
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("TV channels:")
        for i, channel in enumerate(self.channels, start=1):
            print(f"{i}. {channel}")

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel <= len(self.channels):
                channel_name = self.channels[self.channel - 1]
                print(f"TV is on, channel {self.channel} ({channel_name})")
            else:
                print(f"TV is on, channel {self.channel}")
        else:
            print("TV is off")

tv = TV()
channels_list = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"]
tv.set_channels(channels_list)
tv.turn_on()

for new_channel in [1, 3, 7, 4, 2, 5, 8]:
    tv.set_channel(new_channel)
    tv.show_status()