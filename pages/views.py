from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from users.models import Cliente

## 


class HomePageView(TemplateView):
    template_name='pages/home.html'

class ClienteListView(ListView):
    model = Cliente
    template_name = "users/lista_usuarios.html"
    context_object_name = "lista_clientes"


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "users/usuario.html"
    context_object_name = "cliente"

# class ArticleDetailView(DetailView):

#     model = Article

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context



# class ArticleListView(ListView):

#     model = Article
#     paginate_by = 100  # if pagination is desired

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context
