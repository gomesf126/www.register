from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import ClienteBD
from . forms import clienteForm

@login_required
def opcao(request):
	return render(request, 'opcao.html')


@login_required
def listarCliente(request):
	cliente = ClienteBD.objects.all()
	return render(request, 'listar.html' , {'clientes':cliente})


@login_required
def novoCliente(request):
	form = clienteForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('listarCliente')
	return render(request, 'novo.html', {'form':form})


@login_required
def atualizarCliente(request, id):
	cliente = get_object_or_404(ClienteBD, pk=id)
	form = clienteForm(request.POST or None , request.FILES or None, instance=cliente)
	if form.is_valid():
		form.save()
		return redirect(listarCliente)
	return render(request, 'atualizar.html' , {'form':form})

@login_required
def deletarCliente(request, id):
	cliente = get_object_or_404(ClienteBD, pk=id)
	cliente.delete()
	return redirect('listarCliente')

	"""
	from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import ClienteBD
from . forms import clienteForm


@login_required
def person_list(request):
	cliente = ClienteBD.objects.all()	
	return render(request, 'list.html', {'clientes':cliente})


@login_required
def person_new(request):
	form = clienteForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('person_list')
	return render(request, 'new.html', {'form':form})

@login_required
def person_update(request, id):
	cliente = get_object_or_404(ClienteBD, pk=id)
	form = clienteForm(request.POST or None, request.FILES or None, instance=cliente)
	if form.is_valid():
		form.save()
		return redirect('person_list')
	return render(request, 'update.html', { 'form':form} )

@login_required
def person_delete(request, id):
	cliente = get_object_or_404(ClienteBD, pk=id)
	cliente.delete()
	return redirect('person_list')
	"""