from django.shortcuts import render, redirect
from conta.forms import UsuarioForm
from django.contrib.auth import logout
from funcionario.models import Funcionario
from django.shortcuts import render, redirect

def logout_view(request):
    logout(request)
    return redirect('login')

def view_user(request):
    user = request.user
    return render(request, 'funcionario/_base.html', {'user':user})

def perfil(request):
    user = request.user
    if Funcionario.objects.filter(pk=user.id).exists():
        funcionario = Funcionario.objects.get(pk=user.id)
    else:
        funcionario = user

    return render(request, 'registration/perfil.html', {'funcionario': funcionario})
