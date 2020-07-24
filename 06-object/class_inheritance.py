class Car():
    def exclaim(self):
        print("I am a Car!")

class Benz(Car):
    pass

myCar = Car()
myBenz = Benz()

myCar.exclaim()
myBenz.exclaim()