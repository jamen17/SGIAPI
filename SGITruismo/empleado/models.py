from django.db import models

# Create your models here.
from usuarios.models import CustomUser


class Persona(models.Model):
    usuario = models.ForeignKey(CustomUser,null=True,on_delete=models.PROTECT)
    nombres = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    identificacion = models.CharField(primary_key=True)
    tipoPersona = models.CharField(max_lengt=20)#Natural,Juridica.CharField(max_length=100
    clasePersona = models.CharField(max_length=20)#Empleado,Aspirante.CharField(max_length=100
    direccion = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20,default=0)
    email = models.EmailField()
    creacion = models.DateTimeField(auto_now=True)

