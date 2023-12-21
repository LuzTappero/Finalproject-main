from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required


def Home(request):
    return render (request, 'Home/index.html')

def registro_view(request):

    if request.method == "GET":
        return render (request,
                    'Home/registro.html',
                     {"form": UserCreationFormulario()})
    else:
        formulario= UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario= informacion ["username"]
            formulario.save()

            return render (request, 'Home/inicio.html', {"mensaje": f"Usuario creado: {usuario}"})
        else:
            return render (request, 'Home/registro.html', {"form":formulario})

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            'Home/inicio.html',
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            'Home/login.html',
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(request,
                'Home/inicio.html', 
                {"mensaje": f"Bienvenido {usuario}"}) 
        else:
            return render(
                request,
                'Home/login.html',
                {"form": formulario}
            )

def logout_view(request):
    pass