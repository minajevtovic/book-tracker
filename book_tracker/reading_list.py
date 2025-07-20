import json
from pathlib import Path

from book import Book

current_path = Path.cwd()


class ReadingList:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            print(f"The book {book.title} has been added to the reading list")
        else:
            print(f"The book {book.title} is already on the reading list!")

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f"The book {book.title} has been removed from the reading list")
        else:
            print(f"The book {book.title} is not on the list")

    def list_books(self):
        return [book for book in self.books]

    def get_finished_books(self):
        return [book.is_finished for book in self.books if book.is_finished]

    def save_to_json(self):
        book_list = []
        for book in self.books:
            book_list.append(book.to_dict())
        with open("reading_list.json", "w") as f:
            json.dump(book_list, f, indent=2)

    @classmethod
    def load_from_json(cls, path):
        instance = cls()
        with open(path, "r") as f:
            data = json.load(f)

        for book_dict in data:
            instance.books.append(Book.from_dict(book_dict))
        return instance
