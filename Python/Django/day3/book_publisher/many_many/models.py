from django.db import models

# Create your models here.
class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 4:
            errors["title_len"] = "Book title should be at least 4 characters"
        if not postData['title'].islower():
            errors['title_format'] = "You should use lower case letters only"
        if not postData['title'].isalpha():
            errors['title_format_2'] = "You should use letters only, other characters or numbers are not allowed"
        
        return errors

    
class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


class PublisherManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 4:
            errors["name"] = "Publisher name should be at least 4 characters"
        return errors


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PublisherManager()










