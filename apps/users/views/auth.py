from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .utils import CheckEmptyFields, CheckPassword


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if CheckEmptyFields.check_empty_field(username, email, first_name, last_name):
            messages.error(request, 'Fill all fields!')
            return redirect('register')

        if CheckPassword.check_password_lenght(password):
            messages.error(
                request, 'Your password must contain more than 8 digits!')
            if CheckPassword.check_password_corresponds(password, password2):
                messages.error(request, "Your passwords don't match!")
                return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already registered!')
            return redirect('register')

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
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
            username = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(
                request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(
                    request, 'Incorrect e-mail / password! Verify and try again!')
                return redirect('login')

        else:
            messages.error(
                request, 'Incorrect e-mail / password! Verify and try again!')
            return redirect('login')

    else:
        return render(request, 'users/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
