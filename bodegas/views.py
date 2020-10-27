from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime 
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import *
from .models import *
from users.models import *


class BodegaListView(ListView):
    model = Bodega
    template_name = "bodegas/lista_bodegas.html"
    context_object_name = "lista_bodegas"

    def get_queryset(self):
        return Bodega.objects.filter(creador=self.kwargs['id']).order_by('id')


class BodegaDetailView(DetailView):
    model = Bodega
    template_name = "bodegas/bodega.html"
    context_object_name = "bodega"


def CrearBodega(request, id):
    p = "2"
    #usuarios = CustomUser.objects.get(username="henry-leon")
    #print("hola")
    #print (usuarios.id){% url 'lista_bodegas' user.id %}

    prueba = CustomUser.objects.get(pk=id)
    print (prueba)
    print (prueba.id)

    if request.method == 'POST':
        form1 = bodega_forms(request.POST)
        if form1.is_valid():
            print("Empezando")
            bodega = form1.save(commit=False)
            bodega.creador = prueba
            bodega.save()
            print("Exito")
            #messages.success(request, 'Bodega registrada correctamente')
            return HttpResponseRedirect('/lista_bodegas/'+id)
            #return redirect ('home')
    else:
        form1=bodega_forms()
    return render(request,'bodegas/registro_bodega.html',{'form1': form1})


def modificar_bodega(request,id,user_id):
    bodega = Bodega.objects.get(pk=id)
    data = {
        'form': bodega_forms(instance=bodega)
    }
    if request.method=="POST":
        formulario=bodega_forms(data=request.POST, instance=bodega)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Anotacion modificada correctamente"
            data['form'] = formulario
            return HttpResponseRedirect('/lista_bodegas/'+user_id)
    return render(request, 'bodegas/modificar_bodega.html',data)


def eliminar_bodega(request,id,user_id):
    bodega = Bodega.objects.get(pk=id)
    bodega.delete()
    return HttpResponseRedirect('/lista_bodegas/'+user_id)