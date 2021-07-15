from django.db import models
from multiselectfield import MultiSelectField

class AddBook(models.Model):
    MY_CHOICES = (('English', 'English'),
                  ('Hindi', 'Hindi'),
                  )
    BookName=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    Publisher=models.CharField(max_length=200)
    Publication_year=models.IntegerField()
    genre=models.CharField(max_length=240)
    language=MultiSelectField(choices=MY_CHOICES)
    Book_description=models.TextField()


