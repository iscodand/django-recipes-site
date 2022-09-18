from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from recipes.models import Recipes


@login_required(login_url='/users/login')
def dashboard(request):
    user = get_object_or_404(User, pk=request.user.id)

    list_recipes = Recipes.objects.order_by(
        '-datetime').filter(person_name=user)

    data = {
        'recipes': list_recipes
    }

    return render(request, 'users/dashboard.html', data)
