class Car():
    def exclaim(self):
        print("I am a Car!")

class Benz(Car):
    def exclaim(self):
        print("I am a Benz, base on a Car!")
    def need_a_push(self):
        print("A little help here!")

myCar = Car()
myBenz = Benz()

myCar.exclaim()
myBenz.exclaim()
myBenz.need_a_push()