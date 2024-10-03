from django.shortcuts import render, redirect
from .forms import Login, Register, Chat
from .models import ChatTable
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = Chat(request.POST)
        if form.is_valid():
            new_chat = ChatTable.objects.create(usuario=request.user, mensagem=form.cleaned_data['mensagem'])
            new_chat.save()
    else:
        form = Chat()
    context = {
        'form': form,
        'mensagem': [i for i in ChatTable.objects.all()[::-1]]
    }
    return render(request, 'test1_app/index.html', context)

def register(request):
    error = None
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid() and form.cleaned_data['senha'] == form.cleaned_data['confirmar_senha']:
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            new_user = User.objects.create_user(username=usuario, password=senha)
            new_user.save()
            user = authenticate(request, username=usuario, password=senha)
            login(request, user)
            return redirect('index')
        
        elif form.cleaned_data['senha'] != form.cleaned_data['confirmar_senha']:
            error = 'As senhas são diferentes'
            return render(request, 'test1_app/register.html', {'form': form, 'error': error})
        return render(request, 'test1_app/register.html', {'form': form, 'error': error})
    form = Register()
    return render(request, 'test1_app/register.html', {'form': form, 'error': error})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['usuario'], password=form.cleaned_data['senha'])
            if user:
                login(request, user)
                return redirect('index')
            return render(request, 'test1_app/login.html', {'form': form})
    form = Login()
    return render(request, 'test1_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')