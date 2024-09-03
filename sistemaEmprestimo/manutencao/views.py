# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from manutencao.forms import ManutencaoFormRoot, ManutencaoFormFuncionario, ManutencaoConclusaoForm
from .models import Manutencao
from funcionario.models import Funcionario
from django.contrib import messages
from django.utils import timezone

def listar_manutencoes(request):
    funcionario = None
    if request.user.is_superuser:
        manutencoes = Manutencao.objects.all()
    else:
        funcionario = Funcionario.objects.get(id=request.user.id)
        if funcionario.cargo == 1:  # Root
            manutencoes = Manutencao.objects.all()
        else:
            manutencoes = Manutencao.objects.filter(funcionario=funcionario)
    
    return render(request, 'manutencao/listar_manutencoes.html', {'manutencoes': manutencoes, 'funcionario':funcionario})

def criar_manutencao(request):
    funcionario = None
    
    if request.user.is_superuser:
        form = ManutencaoFormRoot(request.POST or None)
    else:
        funcionario = Funcionario.objects.get(id=request.user.id)
        if funcionario.cargo == 1:  # Root
            form = ManutencaoFormRoot(request.POST or None)
        else:
            form = ManutencaoFormFuncionario(request.POST or None)
    
    # Verifica se o formulário é válido
    if form.is_valid():
        manutencao = form.save(commit=False)
        if funcionario is not None:
            manutencao.funcionario = funcionario
        manutencao.save()
        equipamento = form.cleaned_data['equipamento']
        equipamento.iniciarManutencao()    
        return redirect('/manutencao/')

    return render(request, 'manutencao/form_manutencao.html', {'form': form})

def editar_manutencao(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    
    if request.user.is_superuser:
        form = ManutencaoFormRoot(request.POST or None, instance=manutencao)
    else:
        funcionario = Funcionario.objects.get(id=request.user.id)
        if funcionario.cargo == 1:  # Root
            form = ManutencaoFormRoot(request.POST or None, instance=manutencao)
        else:
            if request.user.funcionario != manutencao.funcionario:
                return redirect('manutencao/listar_manutencoes')
            form = ManutencaoFormFuncionario(request.POST or None, instance=manutencao)
    
    if form.is_valid():
        form.save()
        return redirect('manutencao/listar_manutencoes')
    
    return render(request, 'manutencao/editar_manutencao.html', {'form': form})

def concluir_manutencao(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    
    # Verifique se o usuário é um funcionário e obtenha o objeto Funcionario
    try:
        funcionario = Funcionario.objects.get(id=request.user.id)
    except Funcionario.DoesNotExist:
        funcionario = None
    
    # Permitir que o root ou o funcionário responsável concluam a manutenção
    if (funcionario and funcionario != manutencao.funcionario) and request.user.funcionario.cargo != 1:
        return redirect('manutecao/listar_manutencoes')  # Apenas o root ou o funcionário responsável podem concluir
    
    form = ManutencaoConclusaoForm(request.POST or None, instance=manutencao)
    
    if form.is_valid():
        manutencao.concluir_manutencao(
            form.cleaned_data['status'],
            form.cleaned_data.get('observacoesDeConclusao')
        )
        
        
        messages.success(request, 'Manutenção concluída com sucesso!')
        return redirect('/manutencao/')
    
    return render(request, 'manutencao/form_concluir_manutencao.html', {'form': form})

def detalhar_manutencao(request, pk):
    manutencao = Manutencao.objects.get(pk=pk)
    return render(request, 'manutencao/detalhar_manutencao.html', {'manutencao':manutencao})
    
def apagar_manutencao(request, pk):
    emprestimo = Manutencao.objects.get(pk=pk)
    emprestimo.delete()
    return redirect('/manutencao/')