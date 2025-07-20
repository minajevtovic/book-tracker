import typing

Status = typing.Literal["read", "reading", "to_read"]
STATUS = typing.get_args(Status)

ALLOWED_GENRES = [
    "Fiction",
    "Non-Fiction",
    "Science Fiction",
    "Fantasy",
    "Mystery",
    "Biography",
    "Philosophy",
    "History",
    "Romance",
    "Thriller",
    "Self-Help",
    "Classic",
]


class Book:
    status: Status

    def __init__(
        self,
        title: str,
        author: str,
        genre: str | None = None,
        status: Status = "read",
        rating: int | None = None,
    ):
        if status not in STATUS:
            raise ValueError(f"Invalid status '{status}'. Must be one of: {STATUS}")
        if rating is not None:
            if not isinstance(rating, int):
                raise TypeError("Rating should be an integer")
            elif rating not in range(0, 6):
                raise ValueError("Rating should be between 0 and 5")

        self.title = title
        self.author = author
        self._genre = None
        if genre:
            self.genre = genre
        self.status = status
        self.rating = rating

    def __repr__(self):
        return f"title={self.title}, author={self.author}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    @property
    def is_finished(self):
        return self.status == "read"

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value: str):
        if value not in ALLOWED_GENRES:
            raise ValueError(
                f"Genre '{value}' is not allowed. Choose from: {ALLOWED_GENRES}"
            )
        self._genre = value

    def rate_book(self, score: int):
        if self.status != "read":
            raise ValueError("You can only rate already read books.")
        elif not isinstance(score, int):
            raise TypeError("The rating has to be an integer")
        elif score not in range(0, 6):
            raise ValueError("The rating has to be between 0 and 5")
        else:
            self.rating = score

    def to_dict(self):
        book_object = {}
        book_object["title"] = self.title
        book_object["author"] = self.author
        book_object["genre"] = self.genre
        book_object["status"] = self.status
        book_object["rating"] = self.rating

        return book_object

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data["title"],
            author=data["author"],
            genre=data.get("genre"),
            status=data.get("status", "read"),
            rating=data.get("rating"),
        )
