from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Historial_Cambios_FORM,ProductoForm,CategoriaForm,DetalleCategoriasForm,SolicitarTransferenciaForm,DetalleTransferenciasForm,AceptarTransferenciaForm,TerminarTransferenciaForm
from .models import *
# Create your views here.
def Actualizar_Inventario(request):
    print("Hola"+request.method)
    if request.method == 'POST':
        form = Historial_Cambios_FORM(request.POST)
        if form.is_valid():
            product = form.cleaned_data['producto']
            Cant_nueva = form.cleaned_data['cantidad_nueva']
            Motivo = form.cleaned_data['motivo']
            Prod=Producto.objects.get(nombre=product)
            Entrada_Historial=Historial_Cambios
            bodeguero_que_realiza_cambio="Bodeguero Por Defecto"
            print(product)
            print(Cant_nueva)
            historico=Historial_Cambios(
                producto=Prod,
                cantidad_antigua=Prod.cantidad,
                cantidad_nueva=Cant_nueva,
                motivo=Motivo,
                bodeguero=bodeguero_que_realiza_cambio
            )
            historico.save()#Se guarda el historico
            Prod.cantidad=Cant_nueva
            Prod.save()#Se guarda la nueva cantidad en producto

    else:
        form=Historial_Cambios_FORM()
    return render(request,'Productos/Actualizacion_Inventario.html',{'form': form })


def Registrar_producto(request):
    print("HOLA MUNDO"+request.method)
    if request.method == 'POST':
        form1 = ProductoForm(request.POST)
        form2=CategoriaForm(request.POST)
        form3=DetalleCategoriasForm(request.POST)
        if form1.is_valid():
            print("FORM1")
            producto=form1.save(commit=False)
            producto.save()
            messages.success(request, 'Producto registrado correctamente')
            return redirect('Registrar_producto')  
        elif form2.is_valid():
            print("FORM2")
            categoria=form2.save(commit=False)
            categoria.save()
            messages.success(request, 'Categoria registrada correctamente')
            return redirect('Registrar_producto')  
        elif form3.is_valid():
            print("FORM3")
            cat_prod=form3.save(commit=False)
            cat_prod.save()
            messages.success(request, 'Producto agregado a categoria correctamente')
            return redirect('Registrar_producto')  
    else:
        form1=ProductoForm()
        form2=CategoriaForm()
        form3=DetalleCategoriasForm()
    return render(request,'Productos/Registro_producto.html',{'form1': form1,'form2': form2 ,'form3': form3  })


def Historial_productos(request):
    cambios=Historial_Cambios.objects.all()
    return render(request,'Productos/Historial_inventario.html',{'cambios': cambios})

def SolicitarTransferencia(request):
    print("HOLA MUNDO"+request.method)
    if request.method == 'POST':
        form1 = SolicitarTransferenciaForm(request.POST)
        form2=DetalleTransferenciasForm(request.POST)
        if form1.is_valid():
            print("FORM1")
            producto=form1.save(commit=False)
            producto.solicitante="Usuario Bodeguero"
            producto.estado_transferencia="PENDIENTE"
            producto.save()
            messages.success(request, 'Solicitud realizada correctamente, numero transferencia: '+str(producto.pk))
            return redirect('SolicitarTransferencia')  
        elif form2.is_valid():
            print("FORM2")
            categoria=form2.save(commit=False)
            categoria.save()
            messages.success(request, 'Peticion de productos registrada correctamente')
            return redirect('SolicitarTransferencia')  
    else:
        form1=SolicitarTransferenciaForm()
        form2=DetalleTransferenciasForm()
    return render(request,'Productos/SolicitudesTransferencias.html',{'form1': form1,'form2': form2  })

def Ver_solicitudes(request):
    
    Solicitudes=SolicitudTransferenciaProductos.objects.filter(estado_transferencia='PENDIENTE')
    return render(request,'Productos/Aceptar_solicitudes.html',{'Solicitudes': Solicitudes})

def Ver_transferencias(request):
    current_user = request.user
    Solicitudes=SolicitudTransferenciaProductos.objects.filter(estado_transferencia='ACEPTADA',repartidor_asignado = current_user.id)
    return render(request,'Productos/Aceptar_Trasferencias.html',{'Solicitudes': Solicitudes, 'Valor':current_user.id})

def Aceptar_Solicitudes(request,pk):
    if request.method=='POST':
        form=AceptarTransferenciaForm(request.POST)
        if form.is_valid():
            print("asdsad  "+str(pk))
            acept = form.cleaned_data['aceptador']
            soli=SolicitudTransferenciaProductos.objects.get(pk=pk)
            soli.aceptador=acept
            soli.estado_transferencia="ACEPTADA"
            soli.save()
            messages.success(request, 'Se acepto la solicitud '+str(pk)+ ' satisfactoriamente')
            return redirect('Ver_solicitudes')
    if request.method=='GET':
        Solicitudes=SolicitudTransferenciaProductos.objects.filter(estado_transferencia='PENDIENTE')
        Solicitud=SolicitudTransferenciaProductos.objects.get(pk=pk)
        form=AceptarTransferenciaForm()
        return render(request,'Productos/Aceptar_solicitudes.html',{'Solicitud_seleccionada': Solicitud,'Solicitudes': Solicitudes,'form':form})

def Aceptar_Trasferencias(request,pk):
    current_user = request.user
    if request.method=='POST':
        print("asdsad  "+str(pk))
        soli=SolicitudTransferenciaProductos.objects.get(pk=pk)
        soli.estado_transferencia="COMPLETADA"
        soli.save()
        messages.success(request, 'Se acepto la solicitud '+str(pk)+ ' satisfactoriamente')
        return redirect('Ver_transferencias')
    if request.method=='GET':
        print("asdsad  ")
        Solicitudes=SolicitudTransferenciaProductos.objects.filter(estado_transferencia='ACEPTADA',repartidor_asignado = current_user.id)
        Solicitud=SolicitudTransferenciaProductos.objects.get(pk=pk)
        form=TerminarTransferenciaForm()
        return render(request,'Productos/Aceptar_Trasferencias.html',{'Solicitud_seleccionada': Solicitud,'Solicitudes': Solicitudes,'form':form})