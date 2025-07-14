from book import Book
from reading_list import ReadingList

# define example books to be used
book1 = Book(title="1984", author="George Orwell", genre="Dystopian", language="English", status="read", rating=5)
book2 = Book(title="Dune", author="Frank Herbert", genre="Science Fiction", language="English", status="to_read", rating=None)
book3 = Book(title="La Peste", author="Albert Camus", genre="Philosophical Fiction", language="French", status="reading", rating=None)
book4 = Book(title="The Little Prince", author="Antoine de Saint-Exupéry", genre="Fable", language="French", status="read", rating=5)


def test_book():
    assert book1 != book2
    assert book2 == book2
    assert book1.is_finished
    assert book2.is_finished == False
    assert book3.rate_book(3)
    assert "1984" in repr(book1)


def test_reading_list():

    reading_list = ReadingList()
    assert len(reading_list.books) == 0

    reading_list.add_book(book1)
    assert len(reading_list.books) == 1

    reading_list.add_book(book1)
    assert len(reading_list.books) == 1

    reading_list.remove_book(book1)
    assert len(reading_list.books) == 0

    reading_list.add_book(book2)
    reading_list.remove_book(book1)
    assert len(reading_list.books) == 1

    reading_list.add_book(book1)
    reading_list.add_book(book3)
    assert len(reading_list.books) == 3

    finished_books = reading_list.get_finished_books()
    assert len(finished_books) == 1

    
if __name__ == "__main__":
    test_book()
    test_reading_list()
