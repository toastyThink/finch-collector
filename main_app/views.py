from django.shortcuts import render
from .models import Finch 
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# views page functions below
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finch = Finch.objects.all()
    return render(request, 'finches/index.html', 
    {
        'finches': finch
    })

def finches_detail(request, finch_id):
    
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', 
    {
        'finch': finch
    })

#Finch Create View
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

#Finch Update View
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

#Finch Delete View
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

