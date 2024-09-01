from django.shortcuts import render, redirect
from .forms import FuncionarioForm
from .models import Funcionario
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/index.html', {'funcionarios':funcionarios})
    
@login_required
def add(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/funcionario')
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
            return redirect('/funcionario')
    else:
        form = FuncionarioForm(instance=funcionario)
    
    return render(request, 'funcionario/edit.html', {'form':form})
  
@login_required      
def remove(request, funcionarioId):
    funcionario = Funcionario.objects.get(pk=funcionarioId)
    funcionario.delete()
    return redirect('/funcionario')
