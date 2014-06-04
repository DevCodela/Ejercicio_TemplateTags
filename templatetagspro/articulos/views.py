from django.views.generic import ListView
from .models import Articulo

class HomeListView(ListView):

    template_name = 'home.html'
    model = Articulo
    context_object_name = 'articulos'