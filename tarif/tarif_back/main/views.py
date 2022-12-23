from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import orders


def index(request):

 if request.method == 'POST':

    tarif=request.POST['type']
    fio = request.POST['fio']
    telnum = request.POST['telnum']
    email = request.POST['email']

    order = orders(
        tarif=tarif,
        customer=fio,
        phone=telnum,
        email=email,
    )
    order.save()
 return render(request, 'indexpract.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            print(request.POST)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'indexpract.html')
        except:
            orderss = orders.objects.all()
            return render(request, 'admin.html', {'orderss': orderss})
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')


def adminis(request):
    orderss = orders.objects.all()
    return render(request, 'admin.html', {'orderss':orderss})

# Create your views here.
