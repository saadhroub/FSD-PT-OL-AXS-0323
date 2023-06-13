from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import Book, Publisher


def index(request):
    books = Book.objects.all()
    publishers = Publisher.objects.all()
    context = {
        "all_books":books,
        "all_publishers": publishers
    }
    return render(request, "index.html", context)


def create_book(request):
    my_errors = Book.objects.basic_validator(request.POST)
    if len(my_errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else: 
        Book.objects.create(title= request.POST["title"])
        messages.success(request, "Book added successfully")
    return redirect("/")


def create_publisher(request):
    Publisher.objects.create(name= request.POST["name"])
    return redirect("/")

def connection(request):
    book_id  = request.POST["books"]
    publisher_id = request.POST["publishers"]
    book =  Book.objects.get(id=book_id)
    publisher = Publisher.objects.get(id = publisher_id)
    publisher.books.add(book)
    return redirect("/")

