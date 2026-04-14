from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    course=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name
class teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    subject=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    def __str__(self):
        return self.name