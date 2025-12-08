# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 0 
        self.channels = []
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def show_status(self):
        if self.is_on:
            print(f"TV is ON and it displays {self.channel_no} channels")
        else:
            print("TV is OFF")
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels_list):
        self.channels = channels_list
        self.channel_no = len(self.channels)
    def show_channels(self):
        for i in range(len(self.channels)):
            print(f"{i + 1}. {self.channels[i]}")