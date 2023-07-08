import matplotlib.pyplot as plt

class Circle:
    def __init__(self, radius=3, color='red'):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius += r
        return self.radius

    def drawCircle(self):
        circle = plt.Circle((0, 0), self.radius, color=self.color)
        ax = plt.gca()
        ax.add_patch(circle)
        plt.axis('scaled')
        plt.show()

RedCircle = Circle(10, "red")
print(RedCircle.color)
print(RedCircle.radius)
RedCircle.drawCircle()

#LAB
class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
my_car=Car("Audi","RS7","black")
print(my_car.make)
print(my_car.model)
print(my_car.color)

my_car.car_info()

for i in range(2):
    my_car.sell()

my_car.car_info()