from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime 
from django.contrib import messages
from .forms import *
from .models import *
from users.models import *


def CrearBodega(request, id):
    p = "2"
    #usuarios = CustomUser.objects.get(username="henry-leon")
    #print("hola")
    #print (usuarios.id)

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
            messages.success(request, 'Bodega registrada correctamente')
            return redirect ('home')
    else:
        form1=bodega_forms()
    return render(request,'bodegas/registro_bodega.html',{'form1': form1})