from django.db import models

class AddBook(models.Model):
    BookName=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    Publisher=models.CharField(max_length=200)
    Publication_year=models.IntegerField()
    genre=models.CharField(max_length=240)
    language=models.CharField(max_length=290)
    Book_description=models.TextField()


