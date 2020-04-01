from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ClienteForm
from django.contrib import messages

from .models import Cliente

def HelloWord(request):
    return HttpResponse('teste caralho')

@login_required
def ClienteList(request):
    
    search = request.GET.get('search')
    
    if search:
       clientes = Cliente.objects.filter(nome__icontains=search,user=request.user)
    else:
         cliente_list= Cliente.objects.all().order_by('-created_at').filter(user=request.user)
         paginator = Paginator(cliente_list, 3)
         page = request.GET.get('page')
         clientes = paginator.get_page(page)

    return render(request ,'clientes/list.html', {'clientes': clientes})

@login_required
def clientesView(request, id):
    cliente=get_object_or_404(Cliente, pk=id)
    return render(request,'clientes/clientes.html', {'cliente': cliente})

@login_required
def novoCliente(request):
    if request.method=='POST':
        form= ClienteForm(request.POST)

        if form.is_valid():
           cliente=form.save(commit=False)
           cliente.user=request.user
           cliente.save()
           return redirect('/')
    else:
        form=ClienteForm()
        return render(request, 'clientes/addCliente.html',{'form':form})

@login_required
def editarCliente(request, id):
    cliente=get_object_or_404(Cliente, pk=id)
    form= ClienteForm(instance=cliente)
    
    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)
   
        if(form.is_valid()):
           cliente.save()
           return redirect('/')
        else:
           return render(request, 'clientes/editarCliente.html', {'form': form, 'cliente': cliente})
   
    else:
       return render(request, 'clientes/editarCliente.html', {'form': form, 'cliente': cliente})

@login_required
def deletarCliente(request,id):
    cliente=get_object_or_404(Cliente, pk=id)
    cliente.delete()
    messages.info(request, 'Cliente deletado com sucesso.')
    return redirect('/')

