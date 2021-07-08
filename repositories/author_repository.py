from pdb import run
from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.book_repository as book_repository

##save book
def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING * "
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

##select all authors
def select_all():
    authors= []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)
    return authors

##select id
def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        author = Author(result['first_name'], result['last_name'], result['id'])
    return author

##delete all

##delete id

##update book