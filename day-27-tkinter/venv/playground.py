def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum


print(add(4, 5, 7, 2, 1))


def calculate(n, **kwargs):
    print(kwargs)
#    for key, value in kwargs.items():


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
