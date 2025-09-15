from fastapi import APIRouter, status
from typing import List
from .book_schema import Book, BookUpdateModel
from .book_data import books
from fastapi.exceptions import HTTPException

book_router = APIRouter()

@book_router.get('/', response_model=List[Book])
async def get_all_books():
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book)-> dict:
    newBook = book_data.model_dump()
    books.append(newBook)
    return newBook

@book_router.get('/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found!"
    )

@book_router.patch('/{book_id}', status_code=status.HTTP_201_CREATED)
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

@book_router.delete('/{book_id}', status_code=status.HTTP_200_OK)
async def delete_a_book(book_id: int)-> dict:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book Not Found!"
    )
