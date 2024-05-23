import pytest

from libstore.store import Cart


def test_make_empty_cart():
    cart = Cart()
    assert isinstance(cart.get_id(), str)


def test_add_to_cart():
    cart = Cart()
    cart.add_book('123')
    assert cart.get_books() == {'123'}


def test_add_to_cart_multiple():
    cart = Cart()
    cart.add_book('123')
    cart.add_book('333')
    assert cart.get_books() == {'123', '333'}


def test_remove_cart_nonexistent():
    cart = Cart()

    with pytest.raises(ValueError):
        cart.remove_book('123')


def test_remove_cart_works():
    cart = Cart()

    cart.add_book('123')
    cart.remove_book('123')

    assert cart.get_books() == set()
