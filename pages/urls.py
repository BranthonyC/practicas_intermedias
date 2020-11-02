from django.urls import path
from .views import HomePageView, ClienteListView, ClienteDetailView
from producto.views import Actualizar_Inventario,Registrar_producto,Historial_productos,SolicitarTransferencia,Ver_solicitudes,Aceptar_Solicitudes

from gestionVentas.views import Crear_venta,ListaProductosListView,export_pdf,export_pdf2,Agregar_producto

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
    
    ## USUARIO VENDEDOR
    path('crear_ventas/',Crear_venta, name="Crear_venta"),
    path('export_pdf2/<pk>',export_pdf2, name="export_pdf2"),
    
   
]
