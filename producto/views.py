from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Historial_Cambios_FORM,ProductoForm,CategoriaForm,DetalleCategoriasForm
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
