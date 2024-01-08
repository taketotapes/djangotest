from django.urls import path

from .views import books_list, authors_list, genre_detail


urlpatterns = [
    path('', books_list, name='books_list'),
    path('authors', authors_list, name='authors_list'),
    path('books/genres/<int:genre_id>', genre_detail, name='genre_detail'),
]
