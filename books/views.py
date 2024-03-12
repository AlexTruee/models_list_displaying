from django.shortcuts import render

from books.models import Book

from django.core.paginator import Paginator

# def books_view(request):
#     template = 'books/books_list.html'
#     list_book = Book.objects.all()
#     context = {'list_book': list_book}
#     return render(request, template, context)


def books_view(request):
    template = 'books/books_list.html'
    list_book = Book.objects.all()
    context = {'list_book': list_book}
    return render(request, template, context)


def book_date_view(request, pub_date):
    template = 'books/books_date.html'
    try:
        books_next = (Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first())
        if books_next:
            books_next = str(books_next.pub_date)
    except TypeError:
        books_next = None
    try:
        books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
        if books_previous:
            books_previous = str(books_previous.pub_date)
    except TypeError:
        books_previous = None

    context = {
        'books': Book.objects.filter(pub_date__iexact=pub_date),
        'next': books_next,
        'prev': books_previous,
    }
    return render(request, template, context)
