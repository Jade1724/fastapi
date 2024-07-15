from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'maths'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'fiction'},
]

@app.get("/")
async def first_api():
    return {"message": "Hello FastAPI!"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_my_book():
    return {'book_title': 'Title Two'}


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


