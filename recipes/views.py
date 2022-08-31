from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipes


def index(request):
    recipes = Recipes.objects.order_by('-datetime').filter(publicated=True)

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


def search(request):

    list_recipes = Recipes.objects.order_by(
        '-datetime').filter(publicated=True)

    if 'search' in request.GET:
        recipes_to_search = request.GET['search']
        if search:
            list_recipes = list_recipes.filter(
                recipe_name__icontains=recipes_to_search)

    data = {
        'recipes': list_recipes
    }

    return render(request, 'search.html', data)
