from sqlmodel.ext.asyncio.session import AsyncSession
from .book_schema import BookCreateModel, BookUpdateModel

class BookService:
    async def get_all_books(self, session: AsyncSession):
        pass

    async def get_book(self, book_uuid: str ,session: AsyncSession):
        pass

    async def create_book(self, book_data: BookCreateModel ,session: AsyncSession):
        pass

    async def update_book(self, book_uuid: str, book_data: BookUpdateModel, session: AsyncSession):
        pass

    async def delete_book(self, book_uuid: str, session: AsyncSession):
        pass
