from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['Firstname']) < 5:
            errors['Firstname'] = " at least 5 characters"
        if len(postData['Last_name']) < 5:
            errors["Last_name"] = " last name 5 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['mail']):    # test whether a field matches the pattern            
            errors['mail'] = "Invalid email address!"
        if len(postData['Pass']) < 8:
            errors["Pass"] = " password must be at lesat 8 characters"
        if (postData['Pass']) != postData['c-pass']:
            errors['c-pass']="password is note matched "
        return errors


class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    creation=models.ForeignKey(User, related_name="books" ,on_delete=models.CASCADE)   
    favorite=models.ManyToManyField(User,related_name='likes')
    