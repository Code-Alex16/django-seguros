from django.shortcuts import render, redirect
from .forms import ClientesForms
from .models import Clientes
# Create your views here.

def helloWordl(request):
    return render(request, 'hello.html')

def clientes(request):
    list_clientes = Clientes.objects.all()

    return render(request, 'Clientes.html', {'clientes': list_clientes})

def create_clientes(request):

    if request.method == 'GET':

        return render(request, 'create_clientes.html',{
            'form' : ClientesForms
        })

    else:
        try:
            #obtendremos el formulario
            form = ClientesForms(request.POST)
            #creamos un nuevo cliente y solo obtenemos la infromacion para su creacion
            new_cliente = form.save(commit=False)
            new_cliente.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'create_clientes.html', {
                'form' : ClientesForms,
                'error': 'Datos invalidos, ingrese nuevamente datos'
            })

def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')