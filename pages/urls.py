from django.urls import path
from .views import HomePageView, ClienteListView, ClienteDetailView
from producto.views import Actualizar_Inventario,Registrar_producto,Historial_productos,SolicitarTransferencia,Ver_solicitudes,Aceptar_Solicitudes,Ver_transferencias,Aceptar_Trasferencias
from gestionVentas.views import Ver_ventas,Terminar_Venta

from gestionVentas.views import Crear_venta,ListaProductosListView,export_pdf,export_pdf2,Agregar_producto
from bodegas.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('clientes/', ClienteListView.as_view(), name = 'lista_clientes' ),
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name="cliente_detail"),
    path('actualizar_inventario/',Actualizar_Inventario, name="Actualizar_Inventario"),
    path('registrar_producto/',Registrar_producto, name="Registrar_producto"),
    path('historial_productos/',Historial_productos, name="Historial_productos"),
    path('solicitud_transferencias/',SolicitarTransferencia, name="SolicitarTransferencia"),
    path('ver_solicitudes/',Ver_solicitudes, name="Ver_solicitudes"),
    path('ver_solicitudes/<int:pk>',Aceptar_Solicitudes, name="Aceptar_Solicitudes"),
    
    ## USUARIO VENDEDOR MANEJA ESTAS OPCIONES
    path('crear_ventas/',Crear_venta, name="Crear_venta"),
    path('export_pdf2/<pk>',export_pdf2, name="export_pdf2"),
    

    #Solo el Repartidor puede entrar aqui
    path('ver_transferencias/',Ver_transferencias, name="Ver_transferencias"),
    path('ver_transferencias/<int:pk>',Aceptar_Trasferencias, name="Aceptar_Trasferencias"),
    path('ver_ventas/',Ver_ventas, name="Ver_ventas"),
    path('ver_ventas/<int:pk>',Terminar_Venta, name="Terminar_Venta"),

    path('crear_ventas/',Crear_venta, name="Crear_venta"),
    #bodegas
    path('registrar_bodega/<id>',CrearBodega, name="Registrar_bodega"),
    path('lista_bodegas/<id>', BodegaListView.as_view(), name = 'lista_bodegas' ),
    path('bodegas/<int:pk>', BodegaDetailView.as_view(), name="bodega_detail"),
    path('modificar_bodega/<id>/<user_id>', modificar_bodega, name='modificar_bodega'),
    path('eliminar_bodega/<id>/<user_id>', eliminar_bodega, name='eliminar_bodega'),
   
]
