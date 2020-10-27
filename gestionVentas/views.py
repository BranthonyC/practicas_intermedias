from django.shortcuts import render
from django.shortcuts import render, redirect
from producto.models import Producto
from django.http import HttpResponse
from .forms import Historial_Cambios_FORM,NuevaVentaForm,NuevaListaForm,ListaProductosForm
# Create your views here.
from django.contrib import messages
from .models import Venta,ListaProductos
from cliente.models import Cliente

def Crear_venta(request):
    print("Hola"+request.method)
    orden =0
    if request.method == 'POST':
        form = Historial_Cambios_FORM(request.POST)
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
            nueva_orden.save()#Se guarda el historico
            messages.success(request, 'Producto registrado correctamente')
            return redirect('Crear_venta')  
    else:
        #HttpResponse("funciona")
        form=Historial_Cambios_FORM()
        form2=ListaProductosForm()
    return render(request,'ventas/crear_ventas.html',{'form': form,'form2': form2 })

    #return HttpResponse("funciona")

