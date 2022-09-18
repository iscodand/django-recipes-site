from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import Recipes


def index(request):
    recipes = Recipes.objects.order_by('-datetime').filter(publicated=True)

    data = {
        'recipes': recipes
    }

    return render(request, 'recipes/index.html', data)


def recipes(request, recipes_id):
    recipe = get_object_or_404(Recipes, pk=recipes_id)

    recipe_to_show = {
        'recipes': recipe
    }

    return render(request, 'recipes/receita.html', recipe_to_show)


@login_required(login_url='/users/login')
def create_recipes(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        ingredients = request.POST['ingredients']
        preparation_mode = request.POST['preparation_mode']
        preparation_time = request.POST['preparation_time']
        rendiment = request.POST['rendiment']
        category = request.POST['category']
        recipe_picture = request.FILES['recipe_picture']

        user = get_object_or_404(User, pk=request.user.id)
        recipe = Recipes.objects.create(person_name=user, recipe_name=recipe_name, duration=preparation_time, rendiment=rendiment,
                                        category=category, description=preparation_mode, ingredients=ingredients, image=recipe_picture)
        recipe.save()

        return redirect('dashboard')

    else:
        return render(request, 'recipes/recipes_form.html')


@login_required(login_url='/users/login')
def delete_recipes(request, recipes_id):
    recipe = get_object_or_404(Recipes, pk=recipes_id)
    recipe.delete()
    return redirect('dashboard')


@login_required(login_url='/users/login')
def edit_recipes(request, recipes_id):
    recipe = Recipes.objects.get(pk=recipes_id)
    recipe_to_edit = {'recipe' : recipe}
    return render(request, 'recipes/edit_recipes_form.html', recipe_to_edit)


@login_required(login_url='/users/login/')
def update_recipes(request):
    if request.method == 'POST':
        recipe_id = request.POST['recipe_id']
        r = get_object_or_404(Recipes, pk=recipe_id)
        r.recipe_name = request.POST['recipe_name']
        r.ingredients = request.POST['ingredients']
        r.preparation_mode = request.POST['preparation_mode']
        r.preparation_time = request.POST['preparation_time']
        r.rendiment = request.POST['rendiment']
        r.category = request.POST['category']

        if 'recipe_picture' in request.FILES:
            r.recipe_picture = request.FILES['recipe_picture']

        r.save()

        return redirect('dashboard')

    else:
        return redirect('edit_recipes')
