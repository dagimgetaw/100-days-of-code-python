def keyword(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


print(keyword(x=4, y=6, z=8))


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


car = Car(model="Ford", color="Black")
print(car.color)

