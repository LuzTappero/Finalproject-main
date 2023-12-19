from django.db import models

class Blog(models.Model):
    titulo= models.CharField(max_length=255)
    descripcion= models.CharField(max_length=5000)
    autor=models.CharField(max_length=255)
    categoria= models.CharField(max_length=255)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    nombre= models.CharField(max_length=255)
    edad= models.IntegerField()
    comentario= models.TextField(max_length=1000)
    
    def __str__(self):
        return self.comentario
    