from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    data = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html', data)

def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def view_book(request, x):
    book = Book.objects.get(id=x)
    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
    data = {
        "title": book.title,
        "id": book.id,
        "book_author": book.authors.all(),
        "desc": book.desc,
        "authors": Author.objects.all()
    }
    return render(request, 'view-book.html', data)

def authors_index(request):
    data = {
        'authors': Author.objects.all()
    }
    return render(request, 'author.html', data)

def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')

def view_author(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        book_id = request.POST['book_id']
        book = Book.objects.get(id=book_id)
        author.books.add(book)
    data = {
        "first_name": author.first_name,
        "last_name": author.last_name,
        "id": author.id,
        "notes": author.notes,
        "books": author.books.all(),
        "all_books": Book.objects.all()
    }
    return render(request, 'view-author.html', data)