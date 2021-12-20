from Remote import Remote
from TV import TV

class SamsungRemote(Remote):
    def __init__(self, tv):
        super().__init__(tv)

    def button1(self):
        self.television.power()

    def button2(self):
        self.televsion.volume += 5

    def button3(self):
        self.televsion.volume -= 4
        
    def button4(self):
        super().button4()
        print("Explode")
        
    def button5(self):
        print("apple")

if __name__ == "__main__":

    tv1 = TV("Samsung", " 'Smart' TV")
    r1 = SamsungRemote(tv1)
    r1.button1()
    print(tv1.state)
    r1.button2()
    print(tv1.volume)
    r1.button4()
    r1.button5()
