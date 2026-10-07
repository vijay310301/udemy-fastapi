from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel,  Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_year: int

    def __init__(self, id, title, author, description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year


class BookRequest(BaseModel):
    id: Optional[int] = Field(
        description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_year: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "condingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                "published_year": 2001
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby",
         "A very nice book!", 5, 2012),
    Book(2, "Be fast with FastAPI", "codingwithroby", "A great book!", 5, 2001),
    Book(3, "Master Endpoints", "codingwithroby", "A awesome book!", 5, 2000),
    Book(4, "HP1", "Author 1", "Book Description", 2, 2005),
    Book(5, "HP2", "Author 2", "Book Description", 3, 2003),
    Book(6, "HP3", "Author 3", "Book Description", 1, 2008)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    book_by_rating = []
    for book in BOOKS:
        if book.rating == rating:
            book_by_rating.append(book)
    return book_by_rating


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    print(type(book_request))
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def find_book_by_publish_year(published_year: int = Query(gt=1999, ls=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_year == published_year:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            return
    raise HTTPException(status_code=404, detail="Item not found")
        


@app.delete("/books/delete/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")
