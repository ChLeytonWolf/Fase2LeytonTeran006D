from django.shortcuts import render
from . models import Producto, Cliente
from django.views import generic

#formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	num_productos = Producto.objects.all()

	return render(
      request,
        'index.html',
        context={'num_productos':num_productos},

		)



class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['rut','nombres','apellidoP', 'apellidoM', 'fcelular', 'fcasa', 'fecha_nacimiento']
    template_name_suffix = '_update_form'

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('index')

class ClienteDetailView(generic.DetailView):
    model = Cliente


class ClienteListView(generic.ListView):
    model = Cliente
    paginate_by = 20

