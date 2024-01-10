from django.shortcuts import render

from .models import Finch 

# finches = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

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

