from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.recipes, name='receita')
]
