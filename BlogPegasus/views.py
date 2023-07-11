from django.shortcuts import render
from .models import TexTak

# Create your views here.
textt = 'shayannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
def index(request):
    return render(request, 'blog/index.html')

def nav(request):
    sh =TexTak.objects.all()
    for x in sh:
        y = x.mtn1
    return render(request,"blog/home.html", {
        'textt':y
    })
