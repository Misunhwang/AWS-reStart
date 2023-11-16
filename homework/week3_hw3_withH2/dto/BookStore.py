from pydantic import BaseModel, field_validator
from typing import List

from .BookItem import BookItem

class BookStore(BaseModel):
    name: str
    book_shelve: List[BookItem]
