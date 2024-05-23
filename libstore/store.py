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
        self._delivery_statuses = dict()
        self._refund_statuses = dict()

    def add_book(self, book: schemas.Book):
        self._book_catalog[book.name] = book

    def get_book(self, name: str) -> schemas.Book:
        return self._book_catalog[name]

    def start_delivery(self, cart: Cart, _: schemas.DeliveryRequest):
        if cart.get_id() in self._delivery_statuses:
            raise RuntimeError('Cannot restart the delivery of the same cart')

        for name in cart.get_books():
            # Check for existence, might raise
            self._book_catalog[name]

        self._delivery_statuses[cart.get_id()] = schemas.Status.created

    def get_delivery_status(self, cart_id: str) -> schemas.Status:
        return self._delivery_statuses[cart_id]

    def set_delivery_status(self, cart_id: str, status: schemas.Status):
        # Check for existence, might raise
        self._delivery_statuses[cart_id]

        self._delivery_statuses[cart_id] = status

    def start_refund(self, cart_id: str, request: schemas.RefundRequest):
        # Check for existence, might raise
        self._delivery_statuses[cart_id]

        if cart_id in self._refund_statuses:
            raise RuntimeError('Cannot restart a refund')

        self._refund_statuses[cart_id] = schemas.Status.created

    def get_refund_status(self, cart_id: str) -> schemas.Status:
        return self._refund_statuses[cart_id]

    def set_refund_status(self, cart_id: str, status: schemas.Status):
        # Check for existence, might raise
        self._refund_statuses[cart_id]

        self._refund_statuses[cart_id] = status
