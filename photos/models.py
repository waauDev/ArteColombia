from django.db import models
from datetime import date  # Importa el módulo datetime
class Category(models.Model):
    
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True)  # Campo para el lugar de nacimiento
    nacimiento = models.DateField(blank=True, null=True)
    fallecimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Museo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField()
    año_de_fundacion = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Tecnica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)  # Campo para el nombre
    author = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el modelo Autor
    date = models.PositiveIntegerField(null=True, blank=True)
    museum = models.ForeignKey(Museo, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el modelo Museo
    technique = models.ForeignKey(Tecnica, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el modelo
    description = models.TextField()
    
    image = models.ImageField(null=False, blank=False)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'



