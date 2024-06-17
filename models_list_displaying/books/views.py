from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def pub_date_books(request, pub_date):
    try:
        prev = str(Book.objects.filter(pub_date__lt=pub_date).values()[0]['pub_date'])
    except IndexError:
        prev = None
    try:
        next = str(Book.objects.filter(pub_date__gt=pub_date).values()[0]['pub_date'])
    except IndexError:
        next = None
    pub_date = pub_date.strftime('%Y-%m-%d')
    template = 'books/books_by_date.html'
    present_books = Book.objects.filter(pub_date=pub_date)
    context = {
        'books': present_books,
        'prev': prev,
        'next': next,
    }
    return render(request, template, context)
