from django.shortcuts import render

# Create your views here.

def helloWordl(request):
    return render(request, 'hello.html')

def clientes(request):
    return render(request, 'Clientes.html')