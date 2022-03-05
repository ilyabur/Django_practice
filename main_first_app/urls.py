from . import views
from django.urls import path, include

urlpatterns = [
    path('main/', views.index),
    path('about/', views.about)
]
