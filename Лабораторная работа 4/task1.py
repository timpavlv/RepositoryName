class Computer:
    """ Базовый класс компьютеров. """
    def __init__(self, name: str, memory: float, processor_type: str) -> None:
        self.name = name
        self.memory = memory
        self.processor_type = processor_type

    def __str__(self):
        return f"Производитель: {self.name}. Объем памяти: {self.memory}. " \
               f"Процессор: {self.processor_type}\n"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, memory={self.memory!r})"


class Portable_computer(Computer):
    """ Класс портативных компьютеров """
    def __init__(self, name: str, portability_type: str, work_hours: float) -> None:
        super().__init__(name, portability_type)
        self.work_hours = work_hours

    def __str__(self):
        return f"Производитель: {self.name}.Портативность: {self.portability_type}. " \
               f"Время работы не от сети: {self.work_hours}\n"

    def work_hours_dep(self, name: str, work_hours: float):
        """ Время работы не от сети в зависимости от загруженности процессора """
        ...


class Desktop_computer(Computer):
    """ Класс стационарных компьютеров. """
    def __init__(self, name: str, portability_type: str, processor_frequency: str) -> None:
        super().__init__(name, portability_type)
        self.processor_frequency = processor_frequency

    def __str__(self):
        return f"Производитель: {self.name}.Портативность: {self.portability_type}. " \
               f"Частота процессора: {self.processor_frequency}\n"

    def test_render(self, name: str,  portability_type: str, processor_frequency: str):
        """ Время выполнения тестового рендеринга картинки """
        ...


computer1 = Computer("Microsoft", 512, "Intel")
print(computer1.__str__())
print(computer1.__repr__())

#