from book import Book
from reading_list import ReadingList
import typing

print("Welcome to the Book Tracker App. \nHere you can keep a reading list of the books you have " \
"already read, are currently reading or books you want to put on your reading list.\n")
print("Please choose what you want to do:\n" \
"1) Add a new book\n" \
"2) See available books\n" \
"3) Remove a book\n" \
"4) Rate a book\n" \
"5) Leave the application")

reading_list = ReadingList()

while True:

    choice = int(input("Choose your action: "))

    if choice == 1:
        book_title = input("Book title: ")
        author = input("Author: ")
        book = Book(title=book_title, author=author)
        reading_list.add_book(book)

    elif choice == 2:
            print(f"Available books are: {reading_list.list_books()}")

    elif choice == 3: 
            print("Which book would you like to remove from the available ones?\n")
            print(f"Available books are: {reading_list.list_books()}")
            remove_title = input("Book title: ")
            for book in reading_list.books:
                if book.title == remove_title:
                        reading_list.remove_book(book)

    elif choice == 4:
        print("Which book would you like to rate?")
        book_to_rate = input("Type the book name: ")

        found = False
        for book in reading_list.books:
            if book.title == book_to_rate:
                found = True
                try:
                    score = int(input("How would you rate the book (0-5)? "))
                    book.rate_book(score)                        
                except Exception as e:
                      print(f"Error {e}")
                break
        if not found:
            print("Sorry that book is not on the reading list")
                                     
    elif choice == 5:
            print("You're leaving the application. See you next time!")
            break

