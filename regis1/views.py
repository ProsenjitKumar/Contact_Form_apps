from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'regis1/home.html')


def Reg(request):
    return render(request, 'regis1/reg.html')
