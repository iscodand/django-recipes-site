from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('recipe/<int:recipes_id>', recipes, name='receita'),
    path('search', search, name='search'),
    path('create/recipe', create_recipes, name='create_recipes'),
    path('delete/<int:recipes_id>', delete_recipes, name='delete_recipes'),
    path('edit/<int:recipes_id>', edit_recipes, name='edit_recipes'),
    path('update', update_recipes, name='update_recipes'),
]
