from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def recipes(request):
    return render(request, 'receita.html')
