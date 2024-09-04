# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from manutencao.forms import ManutencaoFormRoot, ManutencaoFormFuncionario, ManutencaoConclusaoForm, ManutencaoFormEdit
from .models import Manutencao
from funcionario.models import Funcionario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from equipamento.models import Equipamento

@login_required
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

@login_required
def criar_manutencao(request):
    equipamentosDisponiveis = Equipamento.objects.filter(status=1)

    if not equipamentosDisponiveis.exists():
        messages.warning(request, "No momento, não há equipamentos que necessitem de manutenção.")
        return redirect('/emprestimo/list/')
    
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

'''@login_required
def editar_manutencao(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    
    if request.user.is_superuser:
        form = ManutencaoFormEdit(request.POST or None, instance=manutencao)
    else:
        try:
            funcionario = Funcionario.objects.get(user=request.user)
        except Funcionario.DoesNotExist:
            # Se o Funcionario não existir, redireciona para a lista de manutenções
           return redirect('listar_manutencoes')
        
        if funcionario.cargo == 1:  # Root
            form = ManutencaoFormEdit(request.POST or None, instance=manutencao)
        else:
            if funcionario != manutencao.funcionario:
                return redirect('listar_manutencoes')
            form = ManutencaoFormEdit(request.POST or None, instance=manutencao)
    
    if form.is_valid():
        form.save()
        return redirect('listar_manutencoes')
    
    return render(request, 'manutencao/editar_manutencao.html', {'form': form})
'''

@login_required
def editar_manutencao(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    
    # Tente obter o Funcionario usando o ID do usuário
    try:
        funcionario = Funcionario.objects.get(id=request.user.id)
    except Funcionario.DoesNotExist:
        # Se não for possível encontrar um Funcionario, redirecione
        return redirect('listar_manutencoes')
    
    # Permitir edição se for Root ou se for o responsável pela manutenção
    if request.user.is_superuser or request.user.groups.filter(name='Admin').exists() or funcionario == manutencao.funcionario:
        form = ManutencaoFormEdit(request.POST or None, instance=manutencao)
        
        if form.is_valid():
            form.save()
            return redirect('listar_manutencoes')
        
        return render(request, 'manutencao/editar_manutencao.html', {'form': form})
    else:
        # Se não tiver permissão, redirecione
        messages.error(request, 'Você não tem permissão para editar esta manutenção.')
        return redirect('listar_manutencoes')

@login_required
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

@login_required
def detalhar_manutencao(request, pk):
    manutencao = Manutencao.objects.get(pk=pk)
    return render(request, 'manutencao/detalhar_manutencao.html', {'manutencao':manutencao})
  
@login_required  
def apagar_manutencao(request, pk):
    manutencao = Manutencao.objects.filter(pk=pk).first()
    
    if manutencao:
        equipamento = manutencao.equipamento
        
        # Verifica o status do equipamento e chama o método se necessário
        if equipamento.status == 3:
            equipamento.concluirManutencao()
        
        # Deleta a instância de Manutencao
        manutencao.delete()
    
    # Redireciona após a exclusão ou se Manutencao não for encontrada
    return redirect('/manutencao/')