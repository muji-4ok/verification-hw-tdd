from datetime import datetime

import pytest
from pydantic import ValidationError

from libstore import schemas
from libstore.store import BookStore, Cart


SAMPLE_TIME = datetime(year=1999, month=1, day=1)


@pytest.fixture
def make_sample_book():
    def creator(name: str):
        return schemas.Book(
            name=name,
            author='123',
            publish_date=SAMPLE_TIME,
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


def test_start_delivery(make_sample_book):
    book = make_sample_book('123')

    store = BookStore()
    store.add_book(book)

    cart = Cart()
    cart.add_book('123')
    store.start_delivery(cart, schemas.DeliveryRequest(address='aaa', time=SAMPLE_TIME))

    assert store.get_delivery_status(cart.get_id()) == schemas.Status.created

    store.set_delivery_status(cart.get_id(), schemas.Status.finished)

    assert store.get_delivery_status(cart.get_id()) == schemas.Status.finished


def test_deliver_nonexistent():
    store = BookStore()

    cart = Cart()
    cart.add_book('123')

    with pytest.raises(KeyError):
        store.start_delivery(cart, schemas.DeliveryRequest(address='aaa', time=SAMPLE_TIME))


def test_nonexistent_get_delivery_status():
    store = BookStore()

    with pytest.raises(KeyError):
        store.get_delivery_status('1231231')


def test_nonexistent_set_delivery_status():
    store = BookStore()

    with pytest.raises(KeyError):
        store.set_delivery_status('1231231', schemas.Status.waiting)


@pytest.mark.parametrize('refund', [schemas.RefundRequest(), schemas.RefundRequest(address='123')])
def test_refund_works(make_sample_book, refund: schemas.RefundRequest):
    book = make_sample_book('123')

    store = BookStore()
    store.add_book(book)

    cart = Cart()
    cart.add_book('123')
    store.start_delivery(cart, schemas.DeliveryRequest(address='aaa', time=SAMPLE_TIME))
    store.set_delivery_status(cart.get_id(), schemas.Status.finished)

    store.start_refund(cart.get_id(), refund)

    assert store.get_refund_status(cart.get_id()) == schemas.Status.created

    store.set_refund_status(cart.get_id(), schemas.Status.waiting)

    assert store.get_refund_status(cart.get_id()) == schemas.Status.waiting


def test_refund_nonexistent():
    store = BookStore()

    with pytest.raises(KeyError):
        store.start_refund('12321', schemas.RefundRequest())

    with pytest.raises(KeyError):
        store.get_refund_status('12321')

    with pytest.raises(KeyError):
        store.set_refund_status('12321', schemas.Status.finished)
