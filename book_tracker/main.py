from pathlib import Path

from book import ALLOWED_GENRES, Book
from reading_list import ReadingList


def main():
    print(
        "\n"
        "Welcome to the Book Tracker App. \n\nHere you can keep a reading list of the books you have "
        "already read, are currently reading or books you want to put on your reading list.\n"
    )

    current_path = Path.cwd()
    json_path = current_path / "reading_list.json"

    if json_path.exists():
        reading_list = ReadingList.load_from_json(json_path)
    else:
        reading_list = ReadingList()

    while True:
        try:
            choice = int(
                input(
                    "===================================\n"
                    "Choose your action and press enter: \n"
                    "1) Add a new book\n"
                    "2) See available books\n"
                    "3) Remove a book\n"
                    "4) Rate a book\n"
                    "5) Leave the application\n"
                    "===================================\n"
                )
            )
        except ValueError:
            print("Invalid input: please provide an integer")
            continue

        if choice == 1:
            book_title = input("Book title: ")
            author = input("Author: ")
            book_title = book_title.strip().capitalize()
            author = author.strip().capitalize()
            book = Book(title=book_title, author=author)
            reading_list.add_book(book)

            question_genre = input(
                "Would you like to add a genre of the book? (yes or no) "
            )

            if question_genre.strip().lower() == "yes":
                print(f"Available genres are {ALLOWED_GENRES}")
                while True:
                    try:
                        genre = (
                            input("What is the genre of the book? ")
                            .strip()
                            .capitalize()
                        )
                        book.genre = genre
                        break
                    except ValueError as e:
                        print(f"Error {e}")

            else:
                print("Skipping genre assignment.")

        elif choice == 2:
            print("Available books are: ")
            num = 1
            for book in reading_list.books:
                print(f"{num}. {book.title} by {book.author}")
                num += 1

        elif choice == 3:
            print("Which book would you like to remove from the available ones?\n")
            print(f"Available books are: {reading_list.list_books()}")
            remove_title = input("Book title: ")
            for book in reading_list.books:
                if book.title.lower().strip() == remove_title.lower().strip():
                    reading_list.remove_book(book)

        elif choice == 4:
            print("Which book would you like to rate?")
            book_to_rate = input("Type the book name: ")

            found = False
            for book in reading_list.books:
                if book.title.strip().lower() == book_to_rate.strip().lower():
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
            reading_list.save_to_json()
            print("Your reading list has been saved to 'reading_list.json'.")
            print("You're leaving the application. See you next time!")
            break


if __name__ == "__main__":
    main()
