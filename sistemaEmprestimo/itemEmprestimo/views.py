from django.shortcuts import render, redirect
from .forms import ItemEmprestimoForm
from .models import ItemEmprestimo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

@login_required
def index(request):
    isAdmin = request.user.groups.filter(name='Admin').exists()
    return render(request, 'itemEmprestimo/index.html', {'isAdmin':isAdmin})

@login_required
def add(request):
    if request.method == 'POST':
        form = ItemEmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
           
            # Exibe uma mensagem de sucesso
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return redirect('/itemEmprestimo/list/')
    else:
        form = ItemEmprestimoForm()
    
    return render(request, 'itemEmprestimo/forms.html', {'form':form})
    
@login_required 
def detail(request, itemEmprestimoId):
    itemEmprestimo = ItemEmprestimo.objects.get(pk=itemEmprestimoId)
    return render(request, 'itemEmprestimo/detail.html', {'itemEmprestimo':itemEmprestimo})
 
@login_required    
def edit(request, itemEmprestimoId):
    itemEmprestimo = itemEmprestimo.objects.get(pk=itemEmprestimoId)
    if request.method == 'POST':
        form = ItemEmprestimoForm(request.POST, instance=itemEmprestimo)
        if form.is_valid():
            form.save()
            return redirect('/itemEmprestimo/list')
    else:
        form = ItemEmprestimoForm(instance=itemEmprestimo)
    
    return render(request, 'itemEmprestimo/edit.html', {'form':form})

@login_required
def list(request):
    itemEmprestimos = ItemEmprestimo.objects.all()
    return render(request, 'itemEmprestimo/list.html', {'itemEmprestimos':itemEmprestimos})
  
@login_required      
def remove(request, itemEmprestimoId):
    itemEmprestimo = ItemEmprestimo.objects.get(pk=itemEmprestimoId)
    if request.method == 'POST':
        itemEmprestimo.delete()
        return redirect('/itemEmprestimo/list')
    return render(request, 'itemEmprestimo/confirmar_exclusao.html', {'itemEmprestimo':itemEmprestimo})