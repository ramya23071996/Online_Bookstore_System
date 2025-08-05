from django.shortcuts import render, get_object_or_404
from .models import Author, Category

def author_books(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    return render(request, 'author_books.html', {'author': author, 'books': books})

def category_books(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = category.books.all()
    return render(request, 'category_books.html', {'category': category, 'books': books})

def home(request):
    return render(request, 'home.html')
