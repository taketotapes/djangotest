from django.shortcuts import render
from django.http import HttpResponse

from books.models import Author, Book, Genre


def authors_list(request):
    authors = Author.objects.all()
    context = {'authors': authors, 'title': 'List of authors'}
    return render(request, 'books/author_list.html', context)


def books_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    context = {
        'books': books,
        'genres': genres
    }

    return render(request, 'books/books_list.html')


def genre_detail(request, genre_id):
    return None
