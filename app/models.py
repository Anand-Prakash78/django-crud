from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.TextField(max_length=50)
    lname=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    mob=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)

    
class News(models.Model):
    news_title=models.CharField(max_length=500)
    new_date=models.DateField()
    news_description=models.TextField()
    news_image=models.ImageField(upload_to='static/media/')