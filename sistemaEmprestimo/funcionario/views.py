from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FuncionarioForm
from .models import Funcionario

def index(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/index.html', {'funcionarios':funcionarios})
    
def add(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/funcionario')
    else:
        form = FuncionarioForm()
    
    return render(request, 'funcionario/forms.html', {'form':form})
    
    
def detail(request):
    return HttpResponse('Detail!')
    
def edit(request):
    return HttpResponse('Edit!')
    
def remove(request):
    return HttpResponse('Remove!')
