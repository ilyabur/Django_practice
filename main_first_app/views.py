from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main_first_app/index.html')

def about(request):
    # return HttpResponse("<h4>О нас</h4>") можно так
    return render(request, 'main_first_app/about.html')