from django import forms
from .models import Blog, Comentario

class FormularioBlog(forms.Form):
    titulo= forms.CharField(max_length=255)
    descripcion= forms.CharField(max_length=5000)
    autor=forms.CharField(max_length=255)
    categoria= forms.CharField(max_length=255)

class FormularioBuscarBlog(forms.Form):
    titulo= forms.CharField(max_length=255)
    # autor= forms.CharField(max_length=255)

class FormularioComentario(forms.Form):
    nombre= forms.CharField(max_length=255)
    edad= forms.IntegerField(max_value=120)
    comentario= forms.CharField(max_length=10000)

class FormularioBuscarComentario(forms.Form):
    nombre=forms.CharField(max_length=255)
