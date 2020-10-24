from django.urls import path
from .views import HomePageView, ClienteListView, ClienteDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('clientes/', ClienteListView.as_view(), name = 'lista_clientes' ),
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name="cliente_detail")
]
