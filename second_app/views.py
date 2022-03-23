from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

def news_home(request):
    news = Articles.objects.all() # вместо all можно написть order_by(тайтл или название новости или новость) таким образом мы можем их сортировать
    return render(request, 'second_app/news_home.html', {"news": news})

