from django.shortcuts import render
from . models import Producto
from django.views import generic

# Create your views here.
def index(request):
	num_productos = Producto.objects.all()

	return render(
      request,
        'index.html',
        context={'num_productos':num_productos},

		)