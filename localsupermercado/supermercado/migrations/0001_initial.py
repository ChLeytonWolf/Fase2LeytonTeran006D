# Generated by Django 3.1.2 on 2020-10-16 02:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('cantProductos', models.BigIntegerField()),
                ('monto_base', models.BigIntegerField()),
                ('descuento', models.BigIntegerField(blank=True)),
                ('monto_total', models.BigIntegerField()),
                ('medio', models.CharField(choices=[('D', 'Debito'), ('C', 'Credito'), ('T', 'Transferencia'), ('P', 'PagoSucursal')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=20)),
                ('apellidoM', models.CharField(max_length=20)),
                ('fcelular', models.BigIntegerField(max_length=9)),
                ('fcasa', models.BigIntegerField(max_length=9)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombreC', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombreR', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nombreP', models.CharField(max_length=50)),
                ('stock', models.BigIntegerField(max_length=15)),
                ('precio', models.BigIntegerField(max_length=7)),
                ('imagen', models.ImageField(upload_to='')),
                ('id_tipo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id_direccion', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numeroC', models.BigIntegerField(max_length=6)),
                ('departamento', models.BigIntegerField(max_length=6)),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.comuna')),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supermercado.region'),
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.BigIntegerField()),
                ('id_boleta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.boleta')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.producto')),
            ],
            options={
                'unique_together': {('id_producto', 'id_boleta')},
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id_boleta', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='supermercado.boleta')),
                ('estado', models.CharField(choices=[('Pp', 'Pago pendiente'), ('Re', 'Retirado'), ('An', 'Anulado'), ('En', 'Enviado'), ('Ep', 'Envio pendiente'), ('Rp', 'En espera de retiro'), ('Fa', 'Finalizada')], default='Pago pendiente', max_length=30)),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.direcciones')),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='supermercado.cliente')),
            ],
        ),
    ]