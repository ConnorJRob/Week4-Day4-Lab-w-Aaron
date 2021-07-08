from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
from repositories import book_repository, author_repository

books_blueprint = Blueprint("books", __name__)

# SHOW all
# GET '/books
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("/books/index.html", all_books = books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("/books/new.html", all_authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=['post'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author = author_repository.select(author_id)
    new_book = Book(title, genre, publisher, author)
    book_repository.save(new_book)
    return redirect("/books")

# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("/books/show.html", book=book)


# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['post'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

