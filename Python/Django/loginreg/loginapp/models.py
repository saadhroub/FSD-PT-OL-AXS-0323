from django.db import models
import re
import bcrypt



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if  len(postData['fname']) < 2 or not postData['fname'].isalpha():
            errors["fname"] = "first name should be at least 2 chars and contains letters only"
        if len(postData['lname']) < 2 or not postData['fname'].isalpha():
            errors["lname"] = "last name should be at least 2 chars and contains letters only"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if  len(postData['password']) < 8 :    
            errors['password'] = "THe password must be 8 characters minimum"
        if postData['password'] != postData['pwdconfirm']:
            errors['password'] = "Passwords are note the same"
    
        
        return errors

    def login_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors2 = {}
        email2 = postData['email2']
        password2 = postData['password2']
        usr = User.objects.filter(email=email2)
        if len(email2) < 1:
            errors2["email2"] = "Email cannot be empty!"
        elif not EMAIL_REGEX.match(email2):
            errors2["email2"] = "Invalid Email Address!"
        
        elif not bcrypt.checkpw(password2.encode(), usr[0].password.encode()):
            errors2["password2"] = "Incorrect password. Try again!"
            
        return errors2


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()




