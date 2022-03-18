from django.shortcuts import render
from django.http import HttpResponse

data = {
        "car": "BMW",
        "name": "jus",
        "list": ["Dasha", "Sima", "Yukos"],
        "obj": {
            "name": "Yukos",
            "second_name": "Dasha",
            "third_name": "Sima",
        }
    }

def index(request):
    return render(request, 'main_first_app/index.html', data)

def about(request):
    # return HttpResponse("<h4>О нас</h4>") можно так
    return render(request, 'main_first_app/about.html', data)

def contacts(request):
    return render(request, 'main_first_app/contacts.html', data)