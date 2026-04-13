from django.db import models

# Create your models here.
class student(models.Model):
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