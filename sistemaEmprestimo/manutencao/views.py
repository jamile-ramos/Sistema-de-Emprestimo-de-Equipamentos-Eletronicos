# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from manutencao.forms import ManutencaoFormRoot, ManutencaoFormFuncionario, ManutencaoConclusaoForm
from .models import Manutencao
from funcionario.models import Funcionario

def listar_manutencoes(request):
    funcionario = Funcionario.objects.get(id=request.user.id)
    
    if funcionario.cargo == 1:  # Root
        manutencoes = Manutencao.objects.all()
    else:
        manutencoes = Manutencao.objects.filter(funcionario=request.user.funcionario)
    
    return render(request, 'manutencao/listar_manutencoes.html', {'manutencoes': manutencoes})

def criar_manutencao(request):
    funcionario = Funcionario.objects.get(id=request.user.id)
    
    if funcionario.cargo == 1:  # Root
        form = ManutencaoFormRoot(request.POST or None)
    else:
        form = ManutencaoFormFuncionario(request.POST or None)
    
    # Verifica se o formulário é válido
    if form.is_valid():
        manutencao = form.save(commit=False)
        manutencao.funcionario = funcionario
        manutencao.save()
        return redirect('/manutencao/')

    return render(request, 'manutencao/form_manutencao.html', {'form': form})

def editar_manutencao(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    
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
    
    return render(request, 'manutencao/form_manutencao.html', {'form': form})

def concluir_manutencao(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    
    funcionario = Funcionario.objects.get(id=request.user.id)
    
    if funcionario != manutencao.funcionario and request.user.funcionario.cargo != 1:
        return redirect('manutecao/listar_manutencoes')  # Apenas o root ou o funcionário responsável podem concluir
    
    form = ManutencaoConclusaoForm(request.POST or None, instance=manutencao)
    if form.is_valid():
        manutencao.concluir_manutencao(form.cleaned_data['status'], form.cleaned_data.get('observacoesDeConclusao'))
        return redirect('/manutencao/')
    
    return render(request, 'manutencao/form_concluir_manutencao.html', {'form': form})
