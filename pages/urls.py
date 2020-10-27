from django.urls import path
from .views import HomePageView, ClienteListView, ClienteDetailView
from producto.views import Actualizar_Inventario,Registrar_producto,Historial_productos,SolicitarTransferencia,Ver_solicitudes,Aceptar_Solicitudes,Ver_transferencias,Aceptar_Trasferencias
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

    #Solo el Repartidor puede entrar aqui
    path('ver_transferencias/',Ver_transferencias, name="Ver_transferencias"),
    path('ver_transferencias/<int:pk>',Aceptar_Trasferencias, name="Aceptar_Trasferencias")
]
