import typing

Status = typing.Literal["read","reading", "to_read"]
STATUS = typing.get_args(Status)


class Book:
    status:Status

    def __init__(self, title:str, author:str, genre:str | None = None, language: str | None= None, status:Status = "read", rating:int | None= None):

        if status not in STATUS:
            raise ValueError(f"Invalid status '{status}'. Must be one of: {STATUS}")
        if rating is not None:
            if type(rating) != int:
                raise TypeError("Rating should be an integer")
            elif rating not in range(0,6):
                raise ValueError("Rating should be between 0 and 5")

        self.title = title
        self.author = author
        self.genre = genre 
        self.language = language 
        self.status = status 
        self.rating = rating 

    def __repr__(self):
        return f"title={self.title}, author={self.author}"
    
    def __eq__(self, other):
        if not isinstance(other,Book):
            return False
        return self.title == other.title and self.author == other.author
    
    @property
    def is_finished(self):
        return self.status == "read"

    def rate_book(self, score:int):
        if self.status != "read":
            raise ValueError("You can only rate already read books.")
        elif not isinstance(score,int):
            raise TypeError("The rating has to be an integer")
        elif score not in range(0,6):
            raise TypeError("The rating has to be between 0 and 5")
        else:
            self.rating = score
