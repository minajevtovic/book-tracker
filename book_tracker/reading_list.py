from book import Book

class ReadingList:

    def __init__(self):
        self.books:list[Book] = []

    def add_book(self, book:Book):
        if book not in self.books:
            self.books.append(book)
            print(f"The book {book.title} has been added to the reading list")
        else:
            print(f"The book {book.title} is already on the reading list!")

    def remove_book(self, book:Book):
        if book in self.books:
            self.books.remove(book)
            print(f"The book {book.title} has been removed from the reading list")

        else:
            print(f"The book {book.title} is not on the list")

    def list_books(self):
        return [book for book in self.books]

    def get_finished_books(self):
        return [book.is_finished for book in self.books if book.is_finished]