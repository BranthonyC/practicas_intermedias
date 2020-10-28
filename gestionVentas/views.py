from django.shortcuts import render
from django.shortcuts import render, redirect
from producto.models import Producto
from django.http import HttpResponse
from .forms import Crear_ventaForm,NuevaVentaForm,NuevaListaForm,ListaProductosForm,TerminarVentaForm
# Create your views here.
from django.contrib import messages
from .models import Venta,ListaProductos
from cliente.models import Cliente
## SOLO USUARIOS VENDEDOR PUEDEN CREAR VENTAS
def Crear_venta(request):
    
    orden =0
    if request.method == 'POST':
        form = Crear_ventaForm(request.POST)
        form2 = ListaProductosForm(request.POST)
        if form.is_valid():
            orden = form.data['no_orden']
            cliente = form.cleaned_data['cliente']
            fecha_fac = form.cleaned_data['fecha_facturacion']
            fecha_entr = form.cleaned_data['fecha_entrega']
            tipo_venta_v = form.cleaned_data['tipo_venta']
            #cliente = form.cleaned_data['cliente']
            vendedor_v="Kelvin"
            Clte=Cliente.objects.get(nombre=cliente)
            crear_orden=Venta(
                no_orden= orden,
                cliente=Clte,
                vendedor=vendedor_v,
                fecha_facturacion = fecha_fac,
                fecha_entrega = fecha_entr,
                tipo_venta = tipo_venta_v
                
               
            )
            crear_orden.save()#Se guarda el historico
        if form2.is_valid():
            no_orden2 = form2.cleaned_data['no_orden']
            print("orden" + str(no_orden2))
            producto = form2.cleaned_data['producto']
            cantidad2 = form2.cleaned_data['cantidad']

            Prod=Producto.objects.get(nombre=producto)
            
            nueva_orden=ListaProductos(
                no_orden= no_orden2,
                producto=Prod,
                cantidad=cantidad2,
                precio = Prod.precio,
                subtotal = cantidad2 * float(Prod.precio)
                
               
            )
            nueva_orden.save()
            messages.success(request, 'Producto registrado correctamente')
            return redirect('Crear_venta')  
    else:
        #HttpResponse("funciona")
        form=Crear_ventaForm()
        form2=ListaProductosForm()
    return render(request,'ventas/crear_ventas.html',{'form': form,'form2': form2 })

    #return HttpResponse("funciona")

def Ver_ventas(request):
    current_user = request.user
    Ventas=Venta.objects.filter(estado_venta='PENDIENTE',repartidor_asignado = current_user.id)
    return render(request,'Ventas/Terminar_Venta.html',{'Ventas': Ventas, 'Valor':current_user.id})

def Terminar_Venta(request,pk):
    current_user = request.user
    if request.method=='POST':
        print("asdsad  "+str(pk))
        vent=Venta.objects.get(pk=pk)
        vent.estado_venta="COMPLETADO"
        vent.save()
        messages.success(request, 'Se acepto la solicitud '+str(pk)+ ' satisfactoriamente')
        return redirect('Ver_ventas')
    if request.method=='GET':
        print("asdsad  ")
        Ventas=Venta.objects.filter(estado_venta='PENDIENTE',repartidor_asignado = current_user.id)
        Sell=Venta.objects.get(pk=pk)
        form=TerminarVentaForm()
        return render(request,'Ventas/Terminar_Venta.html',{'Venta_seleccionada': Sell,'Ventas': Ventas,'form':form})