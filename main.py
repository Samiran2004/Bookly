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
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
  {
    "id": 1,
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "publisher": "No Starch Press",
    "publish_date": "2019-05-03",
    "page_count": 544,
    "language": "English"
  },
  {
    "id": 2,
    "title": "Automate the Boring Stuff with Python",
    "author": "Al Sweigart",
    "publisher": "No Starch Press",
    "publish_date": "2019-11-12",
    "page_count": 592,
    "language": "English"
  },
  {
    "id": 3,
    "title": "Python for Data Analysis",
    "author": "Wes McKinney",
    "publisher": "O'Reilly Media",
    "publish_date": "2022-08-30",
    "page_count": 579,
    "language": "English"
  },
  {
    "id": 4,
    "title": "Learning Python",
    "author": "Mark Lutz",
    "publisher": "O'Reilly Media",
    "publish_date": "2013-06-12",
    "page_count": 1648,
    "language": "English"
  },
  {
    "id": 5,
    "title": "Fluent Python",
    "author": "Luciano Ramalho",
    "publisher": "O'Reilly Media",
    "publish_date": "2022-04-01",
    "page_count": 1008,
    "language": "English"
  },
  {
    "id": 6,
    "title": "Head First Python",
    "author": "Paul Barry",
    "publisher": "O'Reilly Media",
    "publish_date": "2016-11-21",
    "page_count": 624,
    "language": "English"
  },
  {
    "id": 7,
    "title": "Python Cookbook",
    "author": "David Beazley",
    "publisher": "O'Reilly Media",
    "publish_date": "2013-05-10",
    "page_count": 706,
    "language": "English"
  },
  {
    "id": 8,
    "title": "Learn Python the Hard Way",
    "author": "Zed A. Shaw",
    "publisher": "Addison-Wesley Professional",
    "publish_date": "2017-06-26",
    "page_count": 320,
    "language": "English"
  },
  {
    "id": 9,
    "title": "Introduction to Machine Learning with Python",
    "author": "Andreas C. Müller",
    "publisher": "O'Reilly Media",
    "publish_date": "2016-09-26",
    "page_count": 400,
    "language": "English"
  },
  {
    "id": 10,
    "title": "Effective Python",
    "author": "Brett Slatkin",
    "publisher": "Addison-Wesley Professional",
    "publish_date": "2019-10-06",
    "page_count": 352,
    "language": "English"
  },
  {
    "id": 11,
    "title": "Python Tricks",
    "author": "Dan Bader",
    "publisher": "Real Python",
    "publish_date": "2017-10-25",
    "page_count": 301,
    "language": "English"
  },
  {
    "id": 12,
    "title": "Hands-On Machine Learning",
    "author": "Aurélien Géron",
    "publisher": "O'Reilly Media",
    "publish_date": "2022-10-15",
    "page_count": 861,
    "language": "English"
  },
  {
    "id": 13,
    "title": "The Quick Python Book",
    "author": "Naomi Ceder",
    "publisher": "Manning Publications",
    "publish_date": "2018-05-15",
    "page_count": 472,
    "language": "English"
  },
  {
    "id": 14,
    "title": "Python Programming for Beginners",
    "author": "Mark Reed",
    "publisher": "CreateSpace Independent",
    "publish_date": "2016-12-29",
    "page_count": 194,
    "language": "English"
  }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

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