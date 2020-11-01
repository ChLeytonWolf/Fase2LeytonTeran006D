from django.test import TestCase
from . models import Cliente

# Create your tests here.

class ClienteModelTest(TestCase):
    @classmethod

    def setUp(self):
        Cliente.objects.create(rut="203920040",apellidoP="Terán")
    
    def test_rut_nombre_cliente(self):
        rutclient=Cliente.objects.get(rut="203920040")
        self.assertEqual(rutclient.apellidoP, "Terán")