from django.shortcuts import render, redirect

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
    Book.objects.create(title= request.POST["title"])
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

