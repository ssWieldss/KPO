from django.shortcuts import render


def index(request):
    return render(request, 'main/data_base.html')

def register(request):
    return render(request, 'main/register.html')

def authorization(request):
    return render(request, 'main/authorization.html')

def creation(request):
    return render(request, 'main/PasCreation.html')
