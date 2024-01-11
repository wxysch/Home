from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request):
    categories=Categories.objects.all()
    context = {
        'title': 'Home-Главная',
        'content' : 'Магазин мебели HOME',
        'categories' : categories,
    }
    return render(request, 'main/base.html',context)

def about(request):
    context = {
        'title' : 'Home - О нас',
        'content' : 'О нас',
        'text_on_page' : 'Какой-то текст блаблаблаблаблаблабла'
    }
    return render(request, 'main/about.html',context)