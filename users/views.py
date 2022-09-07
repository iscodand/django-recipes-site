from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def dashboard(request):
    return render(request)


def register(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not full_name.strip():
            print('Nome não pode estar em branco!')
            return redirect('register')

        if password != password2:
            print('As senhas devem ser iguais!')
            return redirect('register')

        user = User.objects.create_user(
            username=full_name, email=email, password=password)
        user.save()

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado!')
            return redirect('register')

        print(full_name, email, password, password2)
        print('Usuário cadastrado com sucesso!')

        return redirect('login')

    else:
        return render(request, 'users/register.html')


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return render(request)
