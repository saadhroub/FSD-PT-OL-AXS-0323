from django.shortcuts import render, HttpResponse



from .models import Book
# show all of the data from a table
def index(request):
    context = {
    	"all_books": Book.objects.all()
    }
    return render(request, "index.html", context)