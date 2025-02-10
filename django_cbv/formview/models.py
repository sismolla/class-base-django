from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Trial(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=6)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    message = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse("form_views:detail", kwargs={"slug": self.slug})
    

    def save(self,*args,**kwargs):
        if not self.slug:
           self.slug =  slugify(self.title)
        super().save(*args, **kwargs)
