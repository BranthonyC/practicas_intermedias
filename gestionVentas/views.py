from django.shortcuts import render
from django.shortcuts import render, redirect
from producto.models import Producto
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Crear_ventaForm,NuevaVentaForm,NuevaListaForm,ListaProductosForm,Seleccionar_ordenForm,Seleccionar_DetalleForm,Seleccionar_orden2Form,Reportes_Form
from .forms import TerminarVentaForm
# Create your views here.
from django.contrib import messages
from .models import Venta,ListaProductos
from cliente.models import Cliente
from users.models import CustomUser
import random
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import datetime

## SOLO USUARIOS VENDEDOR PUEDEN CREAR VENTAS

## para pdf
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum
from .admin import ListaAdmin

## reportes
from django.views.generic import TemplateView
from django.http import JsonResponse

def Crear_venta(request):
    
    
    orden_random = random.randrange(100000)    
    orden =0
    if request.method == 'POST':
        form = Crear_ventaForm(request.POST)
        form2 = ListaProductosForm(request.POST)
        form4 = Seleccionar_orden2Form(request.POST)
        #form_factura1 = Seleccionar_DetalleForm(request.POST)
        if form.is_valid():
            
            #orden = form.data['no_orden']
            orden = orden_random
            
            cliente = form.cleaned_data['cliente']
            fecha_fac = form.cleaned_data['fecha_facturacion']
            fecha_entr = form.cleaned_data['fecha_entrega']
            tipo_venta_v = form.cleaned_data['tipo_venta']
            
            vendedor_2 = request.user.username
            vendedor_v=vendedor_2
            Clte=Cliente.objects.get(nombre=cliente)
            crear_orden=Venta(
                no_orden= orden_random,
                cliente=Clte,
                vendedor=vendedor_v,
                fecha_facturacion = fecha_fac,
                fecha_entrega = fecha_entr,
                tipo_venta = tipo_venta_v
                
               
            )
            crear_orden.save()#Se guarda el historico

        if form2.is_valid():
            #no_orden2 = form2.cleaned_data['no_orden']
            #print("orden" + str(no_orden2))
            
            producto = form2.cleaned_data['producto']
            cantidad2 = form2.cleaned_data['cantidad']
            porcentaje = form2.cleaned_data['porcentaje']

            Prod=Producto.objects.get(nombre=producto)
            no_orden=Venta.objects.latest('id')
            econtro=ListaProductos.objects.filter(no_orden=no_orden).filter(producto=producto).values()
            
            precio_parcial = cantidad2 * float(Prod.precio)
            precio_real = precio_parcial
            descontar = 1
            if porcentaje == 'SIN_DESCUENTO':
                precio_real
                
            elif porcentaje == 'CINCO':
                print("sdf")
                precio_real = precio_parcial - (precio_parcial * 0.05)
                descontar = 0.05
            elif porcentaje == 'DIEZ':
                precio_real = precio_parcial - (precio_parcial * 0.10)
                print("sdf")
            elif porcentaje == 'QUINCE':
                print("sdf")
                precio_real = precio_parcial - (precio_parcial * 0.15)
            else:
                descontar = 1

            if econtro.count() == 0:
                
                nueva_orden=ListaProductos(
                    no_orden= no_orden,
                    producto=Prod,
                    cantidad=cantidad2,
                    precio = Prod.precio,
                    subtotal = precio_real
                )
                nueva_orden.save()
            else :
                #sub_temp = cantidad2 * float(Prod.precio)
                #sub_temp1 = sub_temp - (sub_temp * descontar)
                modificar_item=ListaProductos.objects.get(no_orden=no_orden,producto=producto)
                modificar_item.cantidad = cantidad2
                modificar_item.subtotal = precio_real
                modificar_item.save()
                messages.success(request, 'Se agrego')
            return redirect('Crear_venta')  
    
        if form4.is_valid():
            
            no_=Venta.objects.latest('id')
            #form_factura1 = Seleccionar_DetalleForm(request.POST)
            #no_ = form4.cleaned_data['no_orden']
            venta=Venta.objects.get(no_orden=no_)
            tipo = venta.tipo_venta
            context = {}
            
            lista_ = ListaProductos.objects.filter(no_orden=no_)
            total = ListaProductos.objects.filter(no_orden=no_).aggregate(Sum('subtotal'))
            total_ = total['subtotal__sum']
            total_descuento = total_
            if tipo == 'DOMICILIO':
                total_descuento = total_descuento  + (total_descuento * 0.10)
            else:
                total_descuento 
            #return HttpResponseRedirect('/lista_detalle/'+str(no_))
            return render(request,'ventas/lista_detalle.html',{'lista_productos' : lista_,'total': total_,'tot_desc':total_descuento,'tipo':tipo,'orden':no_,'cliente':venta.cliente})
            #return redirect('Crear_venta')
        
    else:
        #HttpResponse("funciona")
        form=Crear_ventaForm()
        form2=ListaProductosForm()
        form4=Seleccionar_orden2Form()
    return render(request,'ventas/crear_ventas.html',{'form': form,'form2': form2 ,'form4':form4})
    
def Agregar_producto(request,no_orden):
    
   return HttpResponse("funciona")


class ListaProductosListView(ListView):
    model = ListaProductos
    template_name = "ventas/lista_detalle.html"
    context_object_name = "lista_productos"

    def get_queryset(self):
        return ListaProductos.objects.filter(no_orden=self.kwargs['no_orden'])
   
def export_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'inline; attachment; filename=Sistema_de_BodegasG8_' + str(datetime.datetime.now())+ '.pdf'
    response['Content-Disposition'] = 'attachment; filename=Sistema_de_BodegasG8_' + str(datetime.datetime.now())+ '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    no_o=6892
    #expenses = ListaProductos.objects.filter(no_orden=no_o)
    expenses = ListaProductos.objects.filter(no_orden=no_o)
   
    sum = ListaProductos.objects.aggregate(Sum('subtotal'))
    
    #html_string = render_to_string('ventas/pdf_factura.html',{'expenses':[],'total':0})
    html_string = render_to_string('ventas/pdf_factura.html',{'expenses':expenses,'total':sum})
    #html_string = render_to_string('ventas/pdf_factura.html',{'expenses':expenses})

    html = HTML(string = html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name,'rb')
        response.write(output.read())

    return response

#def export_pdf2(request,pk):
def export_pdf2(request,pk):
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'inline; attachment; filename=Sistema_de_BodegasG8_' + str(datetime.datetime.now())+ '.pdf'
    response['Content-Disposition'] = 'attachment; filename=Sistema_de_BodegasG8_' + str(datetime.datetime.now())+ '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    no_o=40242
    #expenses = ListaProductos.objects.filter(no_orden=no_o)
    expenses = ListaProductos.objects.filter(no_orden=pk)
    venta=Venta.objects.get(no_orden=pk)
    cliente = venta.cliente
    vendedor = venta.vendedor
    fecha_fac  = venta.fecha_facturacion
    fecha_entrega = venta.fecha_entrega

   
    tipo = venta.tipo_venta
    sum = ListaProductos.objects.filter(no_orden=pk).aggregate(Sum('subtotal'))
    sub_total = sum['subtotal__sum']
    total_recargo = sub_total
    if tipo == 'DOMICILIO':
        total_recargo = total_recargo  + (total_recargo * 0.10)
    else:
        total_recargo

    context = {}
    context["cliente"] = cliente
    context["vendedor"] = vendedor
    context["fecha_factura"] = fecha_fac
    context["fecha_entrega"] = fecha_entrega
    context["expenses"] = expenses
    context["sub_total"] = sub_total
    context["total_recargo"] = total_recargo
    context["tipo"] = tipo

    html_string = render_to_string('ventas/pdf_factura.html',context)
    #html_string = render_to_string('ventas/pdf_factura.html',{'expenses':expenses})
    #html_string = render_to_string('ventas/pdf_factura.html',{'expenses':expenses,'total':sub_total,'tipo':tipo,'total_recargo':total_recargo,'context':context})
    

    html = HTML(string = html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name,'rb')
        response.write(output.read())

    return response

    #return redirect('Crear_venta') 
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

### VISTA PARA REPORTES

class VentaReporteView(TemplateView):
    template_name = "ventas/reportes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Venta.objects.all()
        return context

def MostrarReportes(request):
   
    context = {}            
    #total = [1,2,3,4]
    total = []
    clientes = []
    fuck = Cliente.objects.all()
    parametro = []
    vendedores = Venta.objects.values('vendedor').distinct().values()
    
    
    #rep_mes = Venta.objects.filter(fecha_facturacion__month = 6).filter(fecha_facturacion__year = 2021)
    if request.method =='POST':
        form_rep = Reportes_Form(request.POST)
        
        if form_rep.is_valid():
            anio = form_rep.cleaned_data['anio']
            mes = form_rep.cleaned_data['mes']
            semana_ = form_rep.cleaned_data['semana']
            tipo = form_rep.cleaned_data['tipo_rep']
            context['tipo_reporte'] = tipo
            context['anio'] = anio
            context['mes'] = mes
            context['semana'] = semana_
            context['form_rep'] = form_rep
            if tipo == 'mes':
                #total = [1,2,3,4]
                parametro = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','dicimbre']

                for m in range (12):
                    sub_= Venta.objects.filter(fecha_facturacion__month = (m+1)).filter(fecha_facturacion__year=anio).count()
                    total.append(sub_)
                context['total'] = total
                context['cl'] = parametro
                
                return render(request,'ventas/reportes.html',context)
                #return render(request,'ventas/reportes.html',{"total":total,"cl":parametro,'form_rep':form_rep,'context':context})
            elif tipo == 'dia':

                for m in range (30):
                    sub_= Venta.objects.filter(fecha_facturacion__day = (m+1)).filter(fecha_facturacion__month = mes).filter(fecha_facturacion__year=anio).count()
                    if sub_ != 0:
                        total.append(sub_)
                        parametro.append(m+1)
                    else :
                        print("ds")
                context['total'] = total
                context['cl'] = parametro
                return render(request,'ventas/reportes.html',context)
            
            elif tipo == 'semana':
                parametro.append(semana_)
                #parametro= [49]
                sub_= Venta.objects.filter(fecha_facturacion__week=semana_).filter(fecha_facturacion__year=2020).count()
                total.append(sub_)
                context['total'] = total
                context['cl'] = parametro
                return render(request,'ventas/reportes.html',context)
            
            elif tipo == 'vendedor_mes':
                usuarios = request.user.username
                #parametro.append(usuarios)
                parametro = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','dicimbre']
                for m in range (12):
                    sub_= Venta.objects.filter(vendedor=usuarios).filter(fecha_facturacion__month = (m+1)).filter(fecha_facturacion__year=anio).count()
                    total.append(sub_)

                #total_ = Venta.objects.filter(vendedor=usuarios).count()
                #total.append(total_)
                context['total'] = total
                context['cl'] = parametro
                context['vendedor_'] = usuarios
                return render(request,'ventas/reportes.html',context)
            elif tipo == 'vendedor_semana':
                parametro.append(semana_)
                #parametro= [49]
                usuarios = request.user.username
                sub_= Venta.objects.filter(vendedor=usuarios).filter(fecha_facturacion__week=semana_).filter(fecha_facturacion__year=2020).count()
                total.append(sub_)
                context['total'] = total
                context['cl'] = parametro
                context['vendedor_'] = usuarios
                return render(request,'ventas/reportes.html',context)
            else:
                total = [5,6,7,8]
            
        return render(request,'ventas/reportes.html',{"total":total,"cl":parametro,'form_rep':form_rep})
        #return HttpResponse(mes)
        

    if request.method=='GET':
        print("asdsad  ")
        #Ventas=Venta.objects.filter(estado_venta='PENDIENTE',repartidor_asignado = current_user.id)
        #Sell=Venta.objects.get(pk=pk)
        #form=TerminarVentaForm()
        return render(request,'ventas/reportes.html',{"total":total,"cl":fuck})

        


    #return HttpResponse(fuck)
    #return render(request,'ventas/reportes.html',{"total":total,"cl":fuck})
    #return render(request,'ventas/reportes.html',{"total":total,"cl":fuck})
    #return render(request,'ventas/reportes.html',{"context":context})