from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipes


def index(request):
    recipes = Recipes.objects.all()

    data = {
        'recipes' : recipes
    }
    return render(request,'index.html', data)


def recipes(request):
    return render(request, 'receita.html')
