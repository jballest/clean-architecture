from typing import Dict
from src.entities.author import Author
from src.entities.book import Book
from src.repositories.author_repository import AuthorRepository
from src.repositories.book_repository import BookRepository

class AdminCoordinator:
  def __init__(self, book_repository: BookRepository, author_repository: AuthorRepository) -> None:
    self.book_repository = book_repository
    self.author_repository = author_repository

  def create_author(self, author_name: str):
    author = Author(author_name)
    self.author_repository.add(author)

  def create_book(self, book_dict:Dict[str, any]):
    author_id = book_dict.get('author_id')
    self.author_repository.get(author_id)
    book = Book(**book_dict)
    self.book_repository.add(book)

    
