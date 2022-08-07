from django.shortcuts import render
from .models import Book


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)
