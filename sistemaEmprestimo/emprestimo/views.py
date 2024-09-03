from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import EmprestimoForm
from .models import Emprestimo
from django.contrib.auth.decorators import login_required
from itemEmprestimo.models import ItemEmprestimo
from equipamento.models import Equipamento
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'emprestimo/index.html')
    
@login_required
def add(request):
    equipamentosDisponiveis = Equipamento.objects.filter(status=1)

    if not equipamentosDisponiveis.exists():
        messages.warning(request, "Não há equipamentos disponíveis para empréstimo.")
        return redirect('/emprestimo/list/')
    
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, user=request.user)
        if form.is_valid():
            emprestimo = form.save()
            equipamentos = form.cleaned_data['equipamentos']
            
            for equipamento in equipamentos:
                equipamento.emprestar()                
            return redirect('/emprestimo/list/')
    else:
        form = EmprestimoForm(user=request.user)
    
    return render(request, 'emprestimo/forms.html', {'form':form})
    
@login_required 
def detail(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    return render(request, 'emprestimo/detail.html', {'emprestimo':emprestimo})
 
@login_required    
def edit(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados foram alterados com sucesso!')
            return redirect('/emprestimo/list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    
    return render(request, 'emprestimo/edit.html', {'form': form})

@login_required
def list(request):
    emprestimos = Emprestimo.objects.all().distinct()
    return render(request, 'emprestimo/list.html', {'emprestimos':emprestimos})
  
@login_required      
def remove(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    emprestimo.delete()
    return redirect('/emprestimo/list')