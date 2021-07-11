from django import forms

class FormName(forms.Form):
    BookName=forms.CharField()
    Author=forms.CharField()
    Publisher=forms.CharField()
    Publication_year=forms.IntegerField()
    Book_description=forms.CharField(widget=forms.Textarea)
