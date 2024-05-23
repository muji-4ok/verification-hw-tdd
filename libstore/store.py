from libstore import schemas


class Cart:
    def __init__(self):
        pass

    def get_id(self) -> str:
        pass

    def add_book(self, book_name: str):
        pass

    def remove_book(self, book_name: str):
        pass


class BookStore:
    def __init__(self):
        pass

    def add_book(self, book: schemas.Book):
        pass

    def get_book(self, name: str) -> schemas.Book:
        pass

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
