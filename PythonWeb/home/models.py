from django.db import models
from django.conf import settings
# Create your models here.

class TypeFood(models.Model):
    nameTypeFood =  models.CharField(max_length=100)
class Booking(models.Model):
    nameBooking = models.CharField(max_length=100)
    emailBooking = models.CharField(max_length=100)
    phoneBooking = models.CharField(max_length=12)
    checkInBooking = models.DateField()
    timeBooking = models.TimeField() 
    def __str__(self):
        return self.nameBooking
class Food(models.Model):
    nameFood = models.CharField(max_length=100)
    ingredientFood = models.CharField(max_length=100)
    payFood = models.CharField(max_length=100)
    avatarFood = models.ImageField(upload_to='images/foods/') 
    nameTypeFood = models.ForeignKey(TypeFood, on_delete=models.CASCADE)
class MasterChef(models.Model):
    nameChef = models.CharField(max_length=100)
    positionChef = models.CharField(max_length=100)
    selfIntroduceChef = models.CharField(max_length=100)
    avatarChef = models.ImageField(upload_to='images/chefs')
class Blog(models.Model):
    nameBlog = models.CharField(max_length=100)
    posterBlog = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titleBlog = models.CharField(max_length=100)
    contentBlog = models.TextField()
    avatarBlog = models.ImageField(upload_to='images/blogs/') 
    timePost = models.DateTimeField(auto_now_add=True)
    updatedPost = models.DateTimeField(auto_now=True)
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    FullName = models.CharField(max_length=100)
    DOBUser = models.DateField()
    emailUser = models.CharField(max_length=100)
    phoneUser = models.CharField(max_length=12)
    avatarUser = models.ImageField(upload_to='images/users')
    statusUser = models.BooleanField(default=False)
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)