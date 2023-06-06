from django.db import models

from django.db import models
    
class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



new_book = Book(title="Back to Haifa",description="Novel of Palestinian Revolution",release_date="1969-01-21")
new_book.save()


all_books = Book.objects.all()
print(all_books)
