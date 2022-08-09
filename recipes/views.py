from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipes


def index(request):
    recipes = Recipes.objects.all()

    data = {
        'recipes': recipes
    }
    return render(request, 'index.html', data)


def recipes(request, recipes_id):
    recipe = get_object_or_404(Recipes, pk=recipes_id)

    recipe_to_show = {
        'recipes': recipe
    }

    return render(request, 'receita.html', recipe_to_show)
