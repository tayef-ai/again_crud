from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50 , null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    