from django.contrib import admin

# Register your models here.
from . models import Cliente, Region, Comuna, Direcciones, TipoProducto, Producto, Boleta, DetalleBoleta, Compras

admin.site.register(Cliente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direcciones)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
admin.site.register(Compras)