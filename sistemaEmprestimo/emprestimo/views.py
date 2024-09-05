from datetime import datetime, timezone
from django.utils.timezone import now
from django.shortcuts import render, redirect
from .forms import EmprestimoForm, EmprestimoEditForm
from .models import Emprestimo
from django.contrib.auth.decorators import login_required
from funcionario.models import Funcionario
from equipamento.models import Equipamento
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'emprestimo/index.html')

'''
@login_required
def add(request):
    equipamentosDisponiveis = Equipamento.objects.filter(status=1)

    if not equipamentosDisponiveis.exists():
        messages.warning(request, "Não há equipamentos disponíveis para empréstimo.")
        return redirect('/emprestimo/list/')
    
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    emprestimo.funcionario = None
                else:
                    funcionario = Funcionario.objects.get(id=request.user.id)
                    emprestimo.funcionario = funcionario
            
            emprestimo.save()
            
            # Após salvar o emprestimo, associe os equipamentos
            equipamentos = form.cleaned_data['equipamentos']
            emprestimo.equipamentos.set(equipamentos)  # Atualiza a relação muitos-para-muitos
            
            for equipamento in equipamentos:
                equipamento.emprestar()              
              
            return redirect('/emprestimo/list/')
    else:
        form = EmprestimoForm()
    
    return render(request, 'emprestimo/forms.html', {'form':form})
'''

@login_required
def add(request):
    # Filtrar equipamentos que estão com status 'Disponível' (status = 1)
    equipamentosDisponiveis = Equipamento.objects.filter(status=1)

    if not equipamentosDisponiveis.exists():
        messages.warning(request, "Não há equipamentos disponíveis para empréstimo.")
        return redirect('/emprestimo/list/')
    
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            
            if request.user.is_authenticated:
                if request.user.is_superuser:
                    emprestimo.funcionario = None
                else:
                    funcionario = Funcionario.objects.get(id=request.user.id)
                    emprestimo.funcionario = funcionario

            emprestimo.save()
            
            equipamentos = form.cleaned_data['equipamentos']
            emprestimo.equipamentos.set(equipamentos)
            
            # Atualizar status dos equipamentos para "Emprestado" (status = 2)
            for equipamento in equipamentos:
                equipamento.emprestar()  # Atualiza o status para "Emprestado"
              
            return redirect('/emprestimo/list/')
    else:
        form = EmprestimoForm()
    
    return render(request, 'emprestimo/forms.html', {'form': form})

    
@login_required 
def detail(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    return render(request, 'emprestimo/detail.html', {'emprestimo':emprestimo})
 
'''
@login_required    
def edit(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    if request.method == 'POST':
        form = EmprestimoEditForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados foram alterados com sucesso!')
            return redirect('/emprestimo/list')
    else:
        form = EmprestimoEditForm(instance=emprestimo)
    
    return render(request, 'emprestimo/edit.html', {'form': form})
'''
@login_required    
def edit(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    
    if request.method == 'POST':
        form = EmprestimoEditForm(request.POST, instance=emprestimo)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            
            # Verifica o status do empréstimo e atualiza o status dos equipamentos
            equipamentos = emprestimo.equipamentos.all()
            
            if emprestimo.status == Emprestimo.Status.ANDAMENTO:
                # Se o empréstimo está "Em Andamento", todos os equipamentos devem estar "Emprestados"
                for equipamento in equipamentos:
                    equipamento.emprestar()  # Atualiza o status para "Emprestado"
            
            elif emprestimo.status == Emprestimo.Status.CONCLUIDO:
                # Se o empréstimo está "Concluído", todos os equipamentos devem ser "Devolvidos"
                for equipamento in equipamentos:
                    equipamento.devolver()  # Atualiza o status para "Disponível"
                    
            # Salva o empréstimo após atualizar os status dos equipamentos
            emprestimo.save()
            messages.success(request, 'Os dados foram alterados com sucesso!')
            return redirect('/emprestimo/list')
    else:
        form = EmprestimoEditForm(instance=emprestimo)
    
    return render(request, 'emprestimo/edit.html', {'form': form})


@login_required
def list(request):
    emprestimos = Emprestimo.objects.all().distinct()
    return render(request, 'emprestimo/list.html', {'emprestimos':emprestimos})
  
@login_required      
def remove(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    equipamentos = emprestimo.equipamentos.all() 
    
    for equipamento in equipamentos:
        if equipamento.status == 2:
            equipamento.devolver() 
    emprestimo.delete()
    return redirect('/emprestimo/list')

'''
def finish(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    equipamentos = emprestimo.equipamentos.all() 
    
    for equipamento in equipamentos:
        equipamento.devolver() 
        
    # Converte timezone.now() para date para comparar com dataDevolucao
    if now().date() > emprestimo.dataDevolucao:
        emprestimo.status = 3  # Status "Atrasado"
    else:
        emprestimo.status = 1  # Status "Devolvido"
    
    emprestimo.save()
    
    return redirect('/emprestimo/list')
'''

def finish(request, emprestimoId):
    emprestimo = Emprestimo.objects.get(pk=emprestimoId)
    equipamentos = emprestimo.equipamentos.all() 
    
    for equipamento in equipamentos:
        # Verifica se o equipamento está marcado como emprestado (status 2)
        if equipamento.status == 2:
            equipamento.devolver()
        else:
            messages.warning(request, f'O equipamento {equipamento.nome} não está emprestado.')

    # Converte timezone.now() para date para comparar com dataDevolucao
    if now().date() > emprestimo.dataDevolucao:
        emprestimo.status = 3  # Status "Atrasado"
    else:
        emprestimo.status = 1  # Status "Devolvido"

    emprestimo.save()

    return redirect('/emprestimo/list')