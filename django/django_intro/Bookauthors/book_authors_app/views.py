from django.shortcuts import render,redirect
from .models import *
def index(request):
    Data={
        'bks':Book.objects.all()
    }
    return render(request, "index.html", Data)

def addBook(request):
    if request.method=='POST':
        Book.objects.create(title=request.POST['Title'],
                            desc=request.POST['Desc'])
        return redirect('/')
        
def showBook(request, x):
    this_book = Book.objects.get(id=x)
    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = Author.objects.get(id=author_id)
        this_book.authors.add(author)
        this_book.save()

    context = {
        "title": this_book.title,
        "id": this_book.id,
        "book_author": this_book.authors.all(),
        "desc": this_book.desc,
        "authors": Author.objects.all()
    }
    return render(request, 'books.html', context)   
def authors_index(request):
    data = {
        'authors': Author.objects.all()
    }
    return render(request, 'addauthor.html', data)

def addAuthor(request):
    if request.method=="POST":
        Author.objects.create(first_name=request.POST['frst_name'],
                        last_name=request.POST['lst_name'], notes=request.POST['Notes'])
    return redirect('/authors')

def view_authors(request,y):
    author_new=Author.objects.get(id=y)
    if request.method == 'POST':
            book_id = request.POST['book_id']
            book = Book.objects.get(id=book_id)
            author_new.books.add(book)
    data = {
        "first_name":author_new.first_name,
        "last_name": author_new.last_name,
        "id": author_new.id,
        "notes": author_new.notes,
        "books": author_new.books.all(),
        "all_books": Book.objects.all()
    }
    return render(request, 'author.html', data)