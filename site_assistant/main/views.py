from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def registr(request):
    return render(request,'main/register.html')

def product(request):
    return render(request,'main/product.html')