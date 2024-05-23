from datetime import datetime

import pytest

from libstore import schemas
from libstore.store import BookStore


@pytest.fixture
def make_sample_book():
    def creator(name: str):
        return schemas.Book(
            name=name,
            author='123',
            publish_date=datetime(year=1999, month=1, day=1),
            price_rub=1111,
            genre='something',
            publishing_house='house'
        )

    return creator


def test_add_works(make_sample_book):
    store = BookStore()
    book = make_sample_book('123')

    store.add_book(book)
    assert store.get_book('123') == book


def test_get_nonexistent():
    store = BookStore()

    with pytest.raises(KeyError):
        store.get_book('1223')
