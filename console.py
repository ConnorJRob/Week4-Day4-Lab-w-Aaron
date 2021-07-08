import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author("Aaron", "Hall")
author_repository.save(author_1)

author_2 = Author("Connor", "Robertson")
author_repository.save(author_2)

book_1 = Book("Metro 2033", "Horror", "CodeClan", author_1)
book_repository.save(book_1)




