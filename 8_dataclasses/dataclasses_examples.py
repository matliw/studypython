import random
from dataclasses import dataclass, field, replace
from typing import List, Any


def generate_bicycle_cat_number():
    return random.randint(1, 10000)


@dataclass(slots=True)  # SLOTS=True are faster then without SLOTS but do not support inheritance!
class Bicycle:
    name: str
    model: str
    type: str
    wheel_size: float | int
    frame_size: int
    parts: dict[str] = field(default_factory=dict)
    _cat_number: int = field(default_factory=generate_bicycle_cat_number)
    quantity: int = 0  # set default value


@dataclass(frozen=True, kw_only=True)
class FrozenBookRecord:  # read-only, cannot be modified
    title: str
    author: tuple
    cat_number: int = field(default_factory=generate_bicycle_cat_number)


@dataclass(frozen=False, kw_only=True)
class Book:
    title: str
    author: tuple
    cat_number: int = field(default_factory=generate_bicycle_cat_number)
    all_book_data_string: str = field(init=False)  # indicate that this attribute is not part of the initializer and will be contructed later

    def __post_init__(self):
        self.all_book_data_string = f'{self.title} + {self.author} + {self.cat_number}'

    def __repr__(self):
        return f'The book you\'re looking for is {self.title} written by {self.author}'


@dataclass(frozen=False, kw_only=True)
class OtherBook:
    title: str
    author: tuple
    cat_number: int = field(repr=False, default_factory=generate_bicycle_cat_number)  # repr won't print cat_number
    all_book_data_string: str = field(init=False)  # indicate that this attribute is not part of the initializer and will be contructed later

    def __post_init__(self):
        self.all_book_data_string = f'{self.title} + {self.author} + {self.cat_number}'


@dataclass(order=True)  # sorting by specific field
class MyBookCollection:
    sort_index: List[Any] = field(init=False, repr=False)

    title: str
    number_of_pages: int

    def __eq__(self, other: 'MyBookCollection'):
        return self.title == other.title

    def __post_init__(self):
        self.sort_index = [self.number_of_pages, self.title]


if __name__ == '__main__':
    bike = Bicycle('Specialized', 'Chisel', 'XC', 29, 54, {'crankset': 'Shimano'})
    print(bike)
    bike.type = 1
    print(type(bike.parts))
    frozn = FrozenBookRecord(title='Norwegian Wood', author=('Haruki', 'Murakami'))
    #  frozn.author = ('Bill', 'Gates')  # <- frozenbook is read-only
    book = Book(title='Norwegian Wood', author=('Haruki', 'Murakami'))
    book.author = ('J.R.R.', 'Tolkien')
    print(book)
    book2 = OtherBook(title='Dune', author=('Frank', 'Herbert'))
    book2 = replace(book2, title='AAAA')
    print(book2)

    Alice = MyBookCollection(title='Alice', number_of_pages=150)
    Trains = MyBookCollection(title='Trainspotting', number_of_pages=90)
    Zorro = MyBookCollection(title='Zorro', number_of_pages=150)

    # assert (Alice < Zorro) is False
    compare_bool = (Alice < Zorro)
    pass