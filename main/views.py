from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {
        'title': 'Home-Главная',
        'content' : 'Магазин мебели HOME',
    }

    return render(request, 'main/base.html',context)

def about(request):
    context = {
        'title' : 'Home - О нас',
        'content' : 'О нас',
        'text_on_page' : 'Какой-то текст блаблаблаблаблаблабла'
    }
    return render(request, 'main/about.html',context)