from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EquipamentoForm, AtualizarStatusForm
from .models import Equipamento
from django.contrib import messages

# Create your views here.

@login_required
def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/listar_equipamentos.html', {'equipamentos': equipamentos})

@login_required
def criar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            return redirect('/equipamento')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/criar_equipamento.html', {'form': form})

@login_required
def detalhar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    return render(request, 'equipamento/detalhar_equipamento.html', {'equipamento': equipamento})

@login_required
def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados foram alterados com sucesso!')
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    
    return render(request, 'equipamento/editar_equipamento.html', {'form': form})

@login_required
def deletar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    equipamento.delete()
    return redirect('listar_equipamentos')

@login_required
def atualizar_status(request, id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    if request.method == 'POST':
        form = AtualizarStatusForm(request.POST)
        if form.is_valid():
            equipamento.status = form.cleaned_data['novo_status']
            equipamento.save()
            return redirect('equipamento/listar_equipamentos')
    else:
        form = AtualizarStatusForm(initial={'novo_status': equipamento.status})
    return render(request, 'equipamento/criar_equipamento.html', {'form': form})