class Human:
    def __init__(self, name, cpu, ram, video_card, hdd, motherboard, Screen_size,):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.video_card = video_card
        self.hdd = hdd
        self.motherboard = motherboard
        self.Screen_size = Screen_size

    def lowkick(self):
        r = self.name + self.cpu
        return r

laptop = Human('LAPTOP','intel core i5,',"4Gb",'video card','wd740','Super I/O',"1440 x 900")

# print(laptop.name)
# print(laptop.cpu)
# print(laptop.ram)
# print(laptop.video_card)
# print(laptop.hdd)
# print(laptop.motherboard)
# print(laptop.Screen_size)
# print(laptop.lowkick())

def pprint(laptop):
    dict = {"model": laptop.name, "processor": laptop.cpu, "Ram": laptop.ram, "Video Card": laptop.video_card,
    "Hard Disk": laptop.motherboard, "Screen_size": laptop.Screen_size}
    return dict


print(pprint(laptop))