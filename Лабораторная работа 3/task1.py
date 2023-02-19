class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError('Название книги не str')
        self._name = name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author) -> None:
        if not isinstance(author, str):
            raise TypeError('Имя автора не str')
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Число страниц должно выражаться целым числом")
        elif not pages > 0:
            raise ValueError("Число страниц должно выражаться положительным числом")
        else:
            self._pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError('Продолжительность книги должна быть int')
        if duration <= 0:
            raise ValueError('Продолжительность книги должна быть больше 0')
        self._duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"


BOOK = AudioBook("Пресупление и наказание", "Достоевский", 234.0)
print(BOOK.__str__())
#