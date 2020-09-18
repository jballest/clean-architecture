from abc import ABC, abstractmethod
from typing import Dict, Optional
from src.core.entities.book import Book
from src.core.repositories.errors import EntityNotFoundError

class BookRepository(ABC):
  @abstractmethod
  def add(self, book: Book) -> None:
    "Add method to be implemented."
  
  @abstractmethod
  def get(self, uid: str) -> Book:
    "Get method to be implemented."


class MemoryBookRepository(BookRepository):
  def __init__(self) ->None:
    self.books = {}
    self.id_sequence = 1
  
  def add(self, book: Book) -> None:
    book.uid = book.uid or ("B-" + str(self.id_sequence))
    self.books[book.uid] = book
    self.id_sequence += 1

  def get(self, uid: str) -> Book:
    book = self.books.get(uid)
    if not book:
        raise EntityNotFoundError("Book not found.")
    return book

  def load(self, books_dict: Dict[str, Book]) -> None:
    self.books = books_dict
