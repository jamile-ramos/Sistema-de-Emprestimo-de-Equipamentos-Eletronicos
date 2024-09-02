from django.shortcuts import render, redirect
from .models import Usuario
from django.http import HttpResponse
from conta.forms import UsuarioForm
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from funcionario.models import Funcionario
from funcionario.forms import FuncionarioForm

def createUser(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            #cria uma instancia do mudelo usuario a partir dos dados do formulario, mas não salva no bd
            user = form.save(commit=False) 
            user.save()
            
            #adiciona user ao grupo funcionarios
            #user.groups.add(Group.objects.get(name='funcionarios'))
           
            #Chamado para salvar quaisquer relacionamentos many-to-many que o formulário possa ter. Isso é necessário porque commit=False impede que esses relacionamentos sejam salvos automaticamente.
            form.save_m2m()
            
            return redirect('/funcionario/list/') 
    else:
        form = UsuarioForm()
    return render(request, 'registration/register.html', {'form': form})

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


