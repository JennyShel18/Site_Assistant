from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    return redirect('home')


def index(request):
    error=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('product')
        else:
            error = "Неверно введены данные"

    # form = LoginForm()
    context = {
        # 'form': form,
        'error': error
        }
    return render(request,'main/index.html',context)


# def index(request):
#     error = ''
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     error="ok"
#                     return redirect ('product')
#                 else:
#                     error = HttpResponse('Disabled account')
#                     # return redirect('register')
#             else :
#                 return redirect('register')
#         else:
#             error = "Неверно введены данные"
#
#     form = LoginForm()
#     context = {
#             'form': form,
#             'error': error
#     }
#     return render(request,'main/index.html',context)

def registr(request):
    error=''
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="Неверно введены данные"

    form = UserForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request,'main/register.html',context)

@login_required
def product(request):
    return render(request,'main/product.html')