from django.shortcuts import render,redirect
from Books.models import Books
from Books.forms import *

# Create your views here.
def index(request):
    return render(request,'books\index.html')

def ReadBooks(request):
    rows = Books.objects.all()
    return render(request, 'books/readbooks.html', {'rows' : rows})

def ReadBook(request, id):
    try:
        row = Books.objects.get(id = id)
    except Exception:
        row=None
    return render(request, 'books/readbook.html', {'row':row})

def CreateBook(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
        return ReadBooks(request)
    else:
        form = BooksForm()
        return render(request, 'books/createbook.html', {'form' : form} )

def UpdateBook(request, book_id):
    b = Books.objects.get(id=book_id)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance = b)
        if form.is_valid():
            form.save()
        return ReadBooks(request)
    else:
        form = BooksForm(instance = b)
        return render(request, 'books/updatebook.html', {'form' : form} )

def DeleteBook(request, id):
    b = Books.objects.get(id=id)
    if request.method == 'POST':
        b.delete()
        return ReadBooks(request)
    else:
        return render(request, 'books/delete_items.html')

def SearchBook(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['Book_Id']
            return  redirect("/books/readbook/" + str(id))
    else:
        form = BookSearchForm()
    return render(request, 'books/searchbook.html', {'form' : form} )
