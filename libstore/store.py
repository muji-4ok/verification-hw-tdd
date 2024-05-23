import uuid

from libstore import schemas


class Cart:
    def __init__(self):
        self._id = str(uuid.uuid4())
        self._books = set()

    def get_id(self) -> str:
        return self._id

    def add_book(self, book_name: str):
        self._books.add(book_name)

    def remove_book(self, book_name: str):
        self._books.remove(book_name)

    def get_books(self) -> set[str]:
        return self._books


class BookStore:
    def __init__(self):
        self._book_catalog = dict()

    def add_book(self, book: schemas.Book):
        self._book_catalog[book.name] = book

    def get_book(self, name: str) -> schemas.Book:
        return self._book_catalog[name]

    def start_delivery(self, cart: Cart, request: schemas.DeliveryRequest):
        pass

    def get_delivery_status(self, cart_id: str) -> schemas.Status:
        pass

    def set_delivery_status(self, cart_id: str, status: schemas.Status):
        pass

    def start_refund(self, cart_id: str, request: schemas.RefundRequest):
        pass

    def get_refund_status(self, cart_id: str) -> schemas.Status:
        pass

    def set_refund_status(self, cart_id: str, status: schemas.Status):
        pass
