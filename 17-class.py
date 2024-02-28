class Car:
    def __init__(self, brand="Unknown", color="White"):
        self.brand = brand
        self.color = color
        self.wheels = 4

    def start(self):
        print(f"{self.brand} engine started")

    def change_color(self, color):
        self.color = color

    @staticmethod
    def info():
        print("Car object")


class SportsCar(Car):
    def start(self):
        print(f"{self.brand} engine started with 1000 horse power")


Car.info()

print("\n>> Car 1 <<")

car1 = Car("Toyota")
print(f"{car1.brand} brand")
print(f"{car1.color} color")
print(f"{car1.wheels} wheels")

car1.start()
car1.change_color("Red")

print(f"{car1.color} color")

print("\n>> Car 2 <<")

car2 = SportsCar("Ferrari")
print(f"{car2.brand} brand")
print(f"{car2.color} color")
print(f"{car2.wheels} wheels")

car2.start()
