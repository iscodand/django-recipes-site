from django.shortcuts import render


def dashboard(request):
    return render(request)


def register(request):
    return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return render(request)
