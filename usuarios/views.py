from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def usuarios(request):
    return 

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmar_senha')

        if not senha == confirma_senha:
            messages.add_message(request, constants.ERROR, 
                                 'As senha devem ser iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 
                                 'A senha deve conter pelo menos 6 digitos')
            return redirect('/usuarios/cadastro')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 
                                 'Usuário já existente')
            return redirect('/usuarios/cadastro')


        user = User.objects.create_user(username=username, password=senha)
        return redirect('/usuarios/login')
    
def login(request):
    if request.method == 'GET':
        print(request.method)
        return render(request, 'login.html')
    elif request.method == 'POST':
        print(request.method)
        username = request.POST.get('username')
        password = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/empresarios/cadastrar_empresa')
        
        messages.add_message(request, constants.ERROR, 
                             'Usuário ou senha invalidos')
        return redirect('/usuarios/login')

