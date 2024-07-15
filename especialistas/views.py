from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login as login_django
from django.contrib.auth import logout
from django.shortcuts import redirect
from especialistas.forms import EspecialistaForm
from usuario.models import Usuario # type: ignore
from .models import Especialista
from django.contrib.auth.models import Group

#cria especialista novo
#@login_required
#def createespecialista(request):
    # Obtenha o usuário atual
 #   usuario = get_object_or_404(Usuario, username=request.user)
    
    # Verifique se o usuário pertence ao grupo "administrador"
  #  if usuario.groups.filter(name='administrador').exists():
   #     if request.method == 'POST':
    #        form = EspecialistaForm(request.POST)
     #       if form.is_valid():
      #          form.save()
       #         return HttpResponseRedirect("/especialistas/")
        #    else:
         #       form = EspecialistaForm()
          #  return render(request, 'createespecialista.html', {'form': form})
   # else:
    #    return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def createespecialista(request):
    if request.user.groups.filter(name='administrador').exists():
        if request.method == 'POST':
            form = EspecialistaForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/especialistas/")
        else:
            form = EspecialistaForm()
        return render(request, 'createespecialista.html', {'form': form})
    else:
        return render(request, {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def especialistas(request):
    especialistas = Especialista.objects.all()
    return render(request, 'especialistas.html', {'especialistas': especialistas})

@login_required
def updateespecialista(request, id_especialista):
    if request.user.groups.filter(name='administrador').exists():
        especialista = get_object_or_404(Especialista, pk=id_especialista)
        if request.method == 'POST':
            form = EspecialistaForm(request.POST, instance=especialista)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/especialistas/")
        else:
            form = EspecialistaForm(instance=especialista)
        return render(request, 'updateespecialista.html', {'form': form, 'id_especialista': id_especialista})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def deleteespecialista(request, id_especialista):
    if request.user.groups.filter(name='administrador').exists():
        especialista = get_object_or_404(Especialista, pk=id_especialista)
        especialista.delete()
        return HttpResponseRedirect('/especialistas/')
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})

@login_required
def confirmDelete(request, id_especialista):
    if request.user.groups.filter(name='administrador').exists():
        especialista = get_object_or_404(Especialista, pk=id_especialista)
        return render(request, 'confirmdeleteespecialista.html', {'especialista': especialista})
    else:
        return render(request, 'error.html', {'message': 'Você não tem permissão para acessar esta página.'})