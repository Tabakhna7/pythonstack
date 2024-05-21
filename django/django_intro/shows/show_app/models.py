
from django.db import models
import re	


class ShowManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {} 
        if len(postData ['title']) < 2:
            errors['title']="Title must be 3 letters at least !"
        if len(postData ['network']) < 3:
            errors['network']="Network must be 3 letters at least !"    
        if len(postData ['desc']) < 10:
            errors['desc']="Description must be 3 letters at least !"         
        return errors
    
class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

