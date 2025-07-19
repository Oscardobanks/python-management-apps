import json
import math

DATA_FILE = "books.json"


class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = math.ceil(price * 100) / 100  # round up to 2 decimals
        self.stock = stock

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock,
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["price"], data["stock"])


def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump([b.to_dict() for b in books], f)


def load_books():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Book.from_dict(d) for d in data]
    except:
        return []


def search_books(books, search_term):
    results = []
    for b in books:
        if search_term.lower() in b.title.lower() or search_term.lower() in b.author.lower():
            results.append(b)
    return results
