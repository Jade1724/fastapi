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
