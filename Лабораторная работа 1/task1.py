import doctest


class Car:
    def __init__(self, brand: str, year: float, horsepower: float):
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть записана словесно")
        if not isinstance(horsepower, float):
            raise TypeError("Мощность автомобиля должна быть больше 0")
        self.brand = brand
        self.year = year
        self.horsepower = horsepower

    def brand_description(self):
        print(f"Марка - {self.brand}")

    def year_description(self):
        print(f"Год выпуска - {self.year}")

    def horsepower_description(self):
        print(f"Мощность - {self.horsepower}")



class Laptop:
    def __init__(self, screensize: (int, float), weight: (int, float), hours: (int, float)):
        if not isinstance(screensize, (int, float)):
            raise TypeError
        if screensize <= 0:
            raise ValueError
        self.screensize = screensize

        if not isinstance(weight, (int, float)):
            raise TypeError
        if weight <= 0:
            raise ValueError
        self.weight = weight

        if not isinstance(hours, (int, float)):
            raise TypeError
        if hours < 0:
            raise ValueError
        self.hours = hours

    def turn_on(self, turn_on: (int, float)):
        if not isinstance(turn_on, (int, float)):
            raise TypeError
        if turn_on < 0:
            raise ValueError
        ...
    def laptop_is_light(self,  is_light: (int, float)):
        if not isinstance(is_light, (int, float)):
            raise TypeError
        if is_light <= 0:
            raise ValueError


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class Box:
    def __init__(self, material: str, volume: float):
        if not isinstance(material, str):
            raise TypeError
        if not isinstance(volume, float):
            raise TypeError
        if volume <= 0:
            raise ValueError
        self.material = material
        self.volume = volume

    def is_full(self) -> bool:

    def add_stuff(self, add_stuff: float) -> None:

#