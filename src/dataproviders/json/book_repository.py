import json
from src.core.entities.book import Book
from src.core.repositories.errors import EntityNotFoundError
from src.core.repositories.book_repository import BookRepository
from src.dataproviders.json import json_serialize

class JsonBookRepository(BookRepository):
  def __init__(self, filename):
    self.filename = filename

  def add(self, book: Book) -> None:
    with open(self.filename, 'r') as f:
      data = json.load(f)
    sequence = data.get('_sequences', {}).get('books', 1)
    book.uid = book.uid or ("B-" + str(sequence))
    data['books'][author.uid] = vars(book)
    data['_sequences']['books'] = sequence + 1
    with open(self.filename, 'w') as f:
      json.dump(data, f, default=json_serialize)
  
  def get(self, uid: str) -> Book:
    with open(self.filename) as f:
      data = json.load(f)
      books = data.get('books', {})
    book_dict = books.get(uid)
    if not book_dict:
      raise EntityNotFoundError(
          "The project was not found in file.")
    return Book(**book_dict)