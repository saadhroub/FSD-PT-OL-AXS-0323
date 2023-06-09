from django.db import models

from django.db import models
    
class Book(models.Model):
    title = models.CharField(max_length=45)
    pages = models.IntegerField(default=0)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



new_book = Book(title="Back to Haifa",description="Novel of Palestinian Revolution",release_date="1969-01-21")
new_book.save()


Book.objects.create(title="Lord of the Ring",description="Imaginary book",release_date="2004-01-21")
Book.objects.create(title="Animal Farm",description="English Novel",release_date="1999-01-21")


# all_books = Book.objects.all()
# print(all_books)
