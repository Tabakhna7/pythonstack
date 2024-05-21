from django.db import models


import re
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name  should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name  should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "password  should be at least 8 characters" 
        if postData['password']!=postData['password_confirmation']:
            errors['incorrect passowrd']="incorrect password , doesn't match"
        return errors   

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects=UserManager()
    
class Message(models.Model):
    users=models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message=models.TextField()
    time=models.TimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
    users=models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    messages=models.ForeignKey(Message,related_name="comments",on_delete=models.CASCADE)
    comment=models.TextField()
    time=models.TimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)