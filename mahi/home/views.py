from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

# Create your views here.


def landing_page(request):
    person = Data.objects.all()[1]
    return render(request, "home/resume2.html",{"name" : person.name , "title" : person.title})
