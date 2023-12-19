from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Comentario
from .forms import FormularioBlog, FormularioBuscarBlog, FormularioComentario, FormularioBuscarComentario

# def Blog(request):
#     return HttpResponse ('Bienvenidos')

def crear_blog(request):
    if request.method == "GET":
        context= {"form": FormularioBlog()}
        return render(request, 'Blog/crear_blog_formulario.html', context)
    else:
        print (request.POST)
        formulario= FormularioBlog (request.POST)
        if formulario.is_valid():
            informacion_limpia= formulario.cleaned_data
            modelo= Blog(
                titulo=informacion_limpia["titulo"], 
                descripcion=informacion_limpia["descripcion"], 
                autor=informacion_limpia["autor"],
                categoria= informacion_limpia["categoria"]
                )
            modelo.save()
            return render(request, 'Home/index.html')
        
def buscar_blog(request):

    if request.method == "GET":
        form = FormularioBuscarBlog()
        return render(request,
            'Blog/buscar_blog_formulario.html',
            context={"form": form}
        )
    elif request.method == "POST":
        formulario = FormularioBuscarBlog(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            blogs_filtrados = Blog.objects.filter(titulo__icontains=informacion["titulo"])
            context= {"blogs": blogs_filtrados}
            return render (request, 'Blog/blog_list.html', context)
        
    else:
        return render (request, 'Blog/blog_list.html', context={})

def buscar_blog_todos(request):
    blogs= Blog.objects.all()
    return render (request, 'Blog/blog_list.html', {'blogs': blogs})

def crear_comentario(request): 
    if request.method == "GET":
        context= {"form": FormularioComentario()}
        return render(request, 'Blog/crear_comentario_formulario.html', context)
    else:
        print (request.POST)
        formulario= FormularioComentario (request.POST)
        if formulario.is_valid():
            informacion_limpia= formulario.cleaned_data
            modelo= Comentario(
                nombre=informacion_limpia["nombre"], 
                edad=informacion_limpia["edad"], 
                comentario=informacion_limpia["comentario"],

                )
            modelo.save()
            return render(request, 'Home/index.html')
        
def buscar_comentario(request):
    if request.method == "GET":
        form = FormularioBuscarComentario()
        return render(request,
            'Blog/buscar_blog_comentario.html',
            context={"form": form}
        )
    elif request.method == "POST":
        formulario = FormularioBuscarComentario(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            comentarios_filtrados = Comentario.objects.filter(nombre__icontains=informacion["nombre"])
            context= {"comentarios": comentarios_filtrados}
            return render (request, 'Blog/comentario_list.html', context)
        
    else:
        return render (request, 'Blog/comentario_list.html', context={})

def eliminar_blog(request, id):
    if request.method == "POST":

        blog= Blog.objects.get(id=id)
        blog.delete()

        blogs= Blog.objects.all()
        return render (request, 'Blog/blog_list.html', {"blogs": blogs})    
