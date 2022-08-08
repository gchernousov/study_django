from django.shortcuts import render, redirect
from .models import Book


def index(request):
    return redirect('books')

def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def book_pub_date(request, pub_date):
    all_books = Book.objects.order_by('pub_date')
    current_books = all_books.filter(pub_date=pub_date)
    previous_book = all_books.filter(pub_date__lt=pub_date).last()
    next_book = all_books.filter(pub_date__gt=pub_date).first()

    template = 'books/books_pub_date.html'
    context = {
        'books': current_books,
        'previous_book': previous_book,
        'next_book': next_book,
    }
    return render(request, template, context)