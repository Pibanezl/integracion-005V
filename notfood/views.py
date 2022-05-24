from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserForm
from .models import Producto
# Create your views here.


def home(request):
    Productos = Producto.objects.all()
    data = {
        'Productos':Productos
    }
    return render(request, 'notfood/home.html',data)


def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, "registration/registrar.html", data)
