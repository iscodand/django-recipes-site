from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .utils import CheckEmptyFields, CheckPassword

from recipes.models import Recipes

def register(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if CheckEmptyFields.check_empty_field(full_name) or CheckEmptyFields.check_empty_field(email):
            messages.error(request, 'Fill all fields!')
            return redirect('register')

        if CheckPassword.check_password_lenght(password):
            messages.error(request, 'Your password must contain more than 8 digits!')
            if CheckPassword.check_password_corresponds(password, password2):
                messages.error(request, "Your passwords don't match!")
                return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'User already registered!')
            return redirect('register')

        if User.objects.filter(username=full_name).exists():
            messages.error(request, 'User already registered!')
            return redirect('register')

        user = User.objects.create_user(
            username=full_name, email=email, password=password)
        user.save()

        messages.success(request, 'User registered successfully!')

        return redirect('login')

    else:
        return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                print('Login realizado com sucesso!')
                auth.login(request, user)
                return redirect('dashboard')
                
        else:
            print('Crendeciais incorretas!')
            return render(request, 'users/login.html')

    else:
        return render(request, 'users/login.html')


@login_required(login_url='/users/login')
def dashboard(request):
    user = get_object_or_404(User, pk=request.user.id)

    list_recipes = Recipes.objects.order_by(
        '-datetime').filter(person_name=user)

    data = {
        'recipes': list_recipes
    }

    return render(request, 'users/dashboard.html', data)


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
        recipe = Recipes.objects.create(person_name=user, recipe_name=recipe_name, duration=preparation_time, rendiment=rendiment, category=category, description=preparation_mode, ingredients=ingredients, image=recipe_picture)
        recipe.save()
        
        return redirect('dashboard')

    else:
        return render(request, 'users/recipes_form.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

