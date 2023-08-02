from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h1>Страница Django</h1>')

def categories(request, catid):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')