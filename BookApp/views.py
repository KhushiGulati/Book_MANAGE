from django.shortcuts import render
#from . import forms
from .models import AddBook
from django.shortcuts import redirect
def home(request):
    webpage_list=AddBook.objects.all()
    date_dict={'Book_details':webpage_list}
    return render(request,'home.html',context=date_dict)

def form_name_view(request):
    #form=forms.FormName()
    print("hi")
    if request.method == 'POST':
        form1=AddBook()

        form1.BookName=request.POST['BookName']
        form1.Author = request.POST['Author']
        form1.Publisher = request.POST['Publisher']
        form1.Publication_year = request.POST['Publication_year']
        form1.genre= request.POST['genre']
        form1.language= request.POST['language']
        form1.Book_description= request.POST['Book_description']


        form1.save()
        print(form1)
        return redirect('/')



    return render(request,'formtest.html')
