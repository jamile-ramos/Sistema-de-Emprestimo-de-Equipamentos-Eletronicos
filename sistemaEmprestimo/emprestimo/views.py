from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import EmprestimoForm
from .models import Emprestimo
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'emprestimo/index.html')
    
@login_required
def add(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/emprestimo/list/')
    else:
        form = EmprestimoForm()
    
    return render(request, 'emprestimo/forms.html', {'form':form})
    
@login_required 
def detail(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    return render(request, 'emprestimo/detail.html', {'emprestimo':emprestimo})
 
@login_required    
def edit(request, emprestimoId):
    emprestimo = emprestimo.objects.get(pk=emprestimoId)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('/emprestimo/list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    
    return render(request, 'emprestimo/edit.html', {'form':form})

@login_required
def list(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/list.html', {'emprestimos':emprestimos})
  
@login_required      
def remove(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    emprestimo.delete()
    return redirect('/emprestimo/list')