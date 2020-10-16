from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Cliente(models.Model):

	rut = models.CharField(max_length=11, null=False, primary_key=True)
	nombres = models.CharField(max_length=50, null=False)
	apellidoP = models.CharField(max_length=20, null=False)
	apellidoM = models.CharField(max_length=20, null=False)
	fcelular = models.BigIntegerField(max_length=9, null=False)
	fcasa = models.BigIntegerField(max_length=9, null=False)
	fecha_nacimiento= models.DateField(null=False)


	def __str__(self):
		return  (self.nombres+" "+self.apellidoP+" "+self.apellidoM)


	def get_absolute_url(self):
	    return reverse('datos-cliente',arg=[str(self.rut)])

class Region(models.Model):
	id_region=models.UUIDField(primary_key=True,default=uuid.uuid4)
	nombreR=models.CharField(max_length=50,null=False)

	def __str__(self):
		return self.nombreR


class Comuna(models.Model):

	id_comuna= models.UUIDField(primary_key=True,default=uuid.uuid4)
	nombreC = models.CharField(max_length=30,null=False)
	id_region= models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)


	def __str__(self):
		return self.nombreC


class Direcciones(models.Model):

  rut= models.ForeignKey('Cliente', null=False,on_delete=models.RESTRICT)
  id_direccion= models.UUIDField(primary_key=True, default=uuid.uuid4)
  calle=models.CharField(max_length=50, null=False);
  numeroC=models.BigIntegerField(max_length=6, null=False)
  id_comuna = models.ForeignKey('Comuna',null=False,on_delete=models.RESTRICT)
  departamento = models.BigIntegerField(max_length=6)

class TipoProducto(models.Model):

	id_tipo=models.UUIDField(primary_key=True,default=uuid.uuid4)
	tipo=models.CharField(null=False,max_length=50)

	def __str__(self):
		return self.tipo



class Producto(models.Model):
   id_producto=models.UUIDField(primary_key=True,default=uuid.uuid4)
   nombreP=models.CharField(max_length=50,null=False)
   stock=models.BigIntegerField(max_length=15,null=False)
   precio=models.BigIntegerField(max_length=7,null=False)
   imagen=models.ImageField(null=False)
   id_tipo=models.ForeignKey('TipoProducto',null=False,on_delete=models.RESTRICT)

   
   def __str__(self):
   	  return self.nombreP


class Boleta (models.Model):
   id_boleta = models.UUIDField(primary_key=True,default=uuid.uuid4)
   cantProductos= models.BigIntegerField(null=False) 
   monto_base= models.BigIntegerField(null=False)
   descuento=models.BigIntegerField(blank=True)
   monto_total=models.BigIntegerField(null=False)
   loan_pago = ( 
       ('D','Debito'),
       ('C','Credito'),
       ('T','Transferencia'),
       ('P','PagoSucursal'))
   medio = models.CharField(
         max_length=1,
         choices=loan_pago,
         blank=False,
         default='D'

    )

   def __str__(self):
     	return self.monto_total

class DetalleBoleta(models.Model):
	id_producto = models.ForeignKey('Producto',null=False,on_delete=models.RESTRICT)
	id_boleta =models.ForeignKey('Boleta',null=False,on_delete=models.RESTRICT)
	cantidad= models.BigIntegerField(null=False)

	class Meta:
	 	unique_together = (("id_producto","id_boleta"),)


class Compras(models.Model):
	id_boleta=models.ForeignKey('Boleta',primary_key=True,on_delete=models.RESTRICT)
	id_direccion=models.ForeignKey('Direcciones',null=False,on_delete=models.RESTRICT)
	rut=models.ForeignKey('Cliente',null=False,on_delete=models.RESTRICT)
	loan_estado =(
		('Pp','Pago pendiente'),
		('Re','Retirado'),
		('An','Anulado'),
		('En','Enviado'),
		('Ep','Envio pendiente'),
		('Rp','En espera de retiro'),
		('Fa','Finalizada')

		)
	estado= models.CharField(
         max_length=30,
         choices=loan_estado,
         blank=False,
         default='Pago pendiente'
         )

	def __str__(self):
		return self.estado