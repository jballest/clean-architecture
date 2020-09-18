from abc import ABC, abstractmethod
from typing import Dict, Optional
from src.entities.author import Author
from src.repositories.errors import EntityNotFoundError

class AuthorRepository(ABC):
  @abstractmethod
  def add(self, author: Author) -> None:
    "Add method to be implemented."
  
  @abstractmethod
  def get(self, uid: str) -> Author:
    "Get method to be implemented."


class MemoryAuthorRepository(AuthorRepository):
  def __init__(self) ->None:
    self.authors = {}
    self.id_sequence = 1
  
  def add(self, author: Author) -> None:
    author.uid = author.uid or ("A-" + str(self.id_sequence))
    self.authors[author.uid] = author
    self.id_sequence += 1

  def get(self, uid: str) -> Author:
    author = self.authors.get(uid)
    if not author:
        raise EntityNotFoundError("Author not found.")
    return author

  def load(self, authors_dict: Dict[str, Author]) -> None:
    self.authors = authors_dict
