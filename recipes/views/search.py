from django.shortcuts import render
from ..models import Recipes


def search(request):

    list_recipes = Recipes.objects.order_by(
        '-datetime').filter(publicated=True)

    if 'search' in request.GET:
        recipes_to_search = request.GET['search']
        list_recipes = list_recipes.filter(recipe_name__icontains=recipes_to_search)

    data = {
        'recipes': list_recipes
    }

    return render(request, 'recipes/search.html', data)