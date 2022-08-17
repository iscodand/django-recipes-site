from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipes_id>', views.recipes, name='receita'),
    path('search', views.search, name='search'),
]
