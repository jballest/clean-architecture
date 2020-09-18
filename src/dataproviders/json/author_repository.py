import json
from src.core.entities.author import Author
from src.core.repositories.errors import EntityNotFoundError
from src.core.repositories.author_repository import AuthorRepository
from src.dataproviders.json import json_serialize

class JsonAuthorRepository(AuthorRepository):
  def __init__(self, filename):
    self.filename = filename

  def add(self, author: Author) -> None:
    with open(self.filename, 'r') as f:
      data = json.load(f)
    sequence = data.get('_sequences', {}).get('authors', 1)
    author.uid = author.uid or ("A-" + str(sequence))
    data['authors'][author.uid] = vars(author)
    data['_sequences']['authors'] = sequence + 1
    with open(self.filename, 'w') as f:
      json.dump(data, f, default=json_serialize)
  
  def get(self, uid: str) -> Author:
    with open(self.filename) as f:
      data = json.load(f)
      authors = data.get('authors', {})
    author_dict = authors.get(uid)
    if not author_dict:
      raise EntityNotFoundError(
          "The project was not found in file.")
    return Author(**author_dict)