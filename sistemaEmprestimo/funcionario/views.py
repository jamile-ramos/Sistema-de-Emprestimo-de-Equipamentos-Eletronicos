from django.shortcuts import render, redirect
from .forms import FuncionarioForm
from .models import Funcionario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

@login_required
def index(request):
    isAdmin = request.user.groups.filter(name='Admin').exists()
    return render(request, 'funcionario/index.html', {'isAdmin':isAdmin})

@login_required
def add(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save()
            
            grupo_funcionarios = Group.objects.get(name='Funcionarios')
            funcionario.groups.add(grupo_funcionarios)
            
            # Exibe uma mensagem de sucesso
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return redirect('/funcionario/list/')
    else:
        form = FuncionarioForm()
    
    return render(request, 'funcionario/forms.html', {'form':form})
    
@login_required 
def detail(request, funcionarioId):
    funcionario = Funcionario.objects.get(pk=funcionarioId)
    return render(request, 'funcionario/detail.html', {'funcionario':funcionario})
 
@login_required    
def edit(request, funcionarioId):
    funcionario = Funcionario.objects.get(pk=funcionarioId)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('/funcionario/list')
    else:
        form = FuncionarioForm(instance=funcionario)
    
    return render(request, 'funcionario/edit.html', {'form':form})

@login_required
def list(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/list.html', {'funcionarios':funcionarios})
  
@login_required      
def remove(request, funcionarioId):
    funcionario = Funcionario.objects.get(pk=funcionarioId)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('/funcionario/list')
    return render(request, 'funcionario/confirmar_exclusao.html', {'funcionario':funcionario})