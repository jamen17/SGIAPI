from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    tipoId = models.CharField(max_length=20)
    identificacion = models.CharField(max_length=20,unique=True)
    regimen = models.CharField(max_length=20)
    web = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    logo = models.CharField(max_length=150)
    creacion = models.DateTimeField(auto_now=True)


class Sucursal(models.Model):
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20)
    creacion = models.DateTimeField(auto_now=True)

class Dependencia(models.Model):
    sucursal = models.ForeignKey(Sucursal,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)

class Cargo(models.Model):
    dependencia = models.ForeignKey(Dependencia,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    salario = models.IntegerField(default=0)
    horas = models.IntegerField(default=0)

class Competencia(models.Model):
    cargo = models.ForeignKey(Cargo,on_delete=models.PROTECT)
    competencia = models.CharField(max_length=150)




