from django.db import models
from django.urls import reverse

# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name




class Peoples (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True ,null=True)
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120)
    content = models.TextField()
    img = models.ImageField(upload_to ='upload', blank= True,null =True)
    
    def __str__(self):
        return self.category
    def __str__(self):
        return self.title
    def __str__(self):
        return self.sub_title
    def __str__(self):
        return self.content


class Projects(models.Model):
    title =   models.CharField(max_length=120)
    imgs = models.ImageField(upload_to ='upload', blank= True,null =True)
    body = models.TextField()



class Servises (models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class AddPost(models.Model):
    name = models.CharField(max_length=120)
    phone = models.IntegerField(max_length=14)
    category = models.ForeignKey(Servises, on_delete=models.CASCADE, default=True ,null=True, blank=True)
    massage =models.TextField()
    
    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.name
    def __str__(self):
        return self.massage
    def __str__(self):
        return self.category 
    def __str__(self):
        return self.massage       
