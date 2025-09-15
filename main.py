# from fastapi import FastAPI, Header
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()

# @app.get('/')
# async def read_root():
#     return {
#         "message": "Hello World!"
#     }

# @app.get('/greet') # http://localhost:8000/greet/Samiran?age=21
# async def greet(name: Optional[str] = "User",
#                 age: int = 0) -> dict:
#     return {
#         "message": f"Hello {name}, age: {age}"
#     }

# class BookCreateModel(BaseModel):
#     title: str
#     author: str

# @app.post('/create_book')
# async def create_book(book_data: BookCreateModel):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }

# @app.get('/get_headers', status_code=201)
# async def getHeaders(
#     accept:str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)
# ):
#     req_headers = {}
#     req_headers["Accept"] = accept
#     req_headers["Content-Type"] = content_type
#     req_headers["User-Agent"] = user_agent
#     req_headers["Host"] = host
#     return req_headers

#### -------------------------------------------- ####

from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from typing import List
from book_schema import Book, BookUpdateModel
from book_data import books

app = FastAPI()

@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book)-> dict:
    newBook = book_data.model_dump()
    books.append(newBook)
    return newBook

@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found!"
    )

@app.patch('/book/{book_id}', status_code=status.HTTP_201_CREATED)
async def update_book(book_id: int, book_update_data: BookUpdateModel)-> dict:

    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['author'] = book_update_data.author
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found!"
    )

@app.delete('/book/{book_id}', status_code=status.HTTP_200_OK)
async def delete_a_book(book_id: int)-> dict:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found!"
    )
