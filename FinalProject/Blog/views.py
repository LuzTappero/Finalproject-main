from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Comentario
from .forms import FormularioBlog, FormularioBuscarBlog, FormularioComentario, FormularioBuscarComentario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
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

def editar_blog(request, id):


    blog = Blog.objects.get(id=id)

    if request.method == "POST":
        miFormulario= FormularioBlog(request.POST)

        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            
            blog.titulo= informacion["titulo"]
            blog.descripcion = informacion["informacion"]
            blog.autor = informacion["autor"]
            blog.categoria = informacion["categoria"]
            blog.save()

            return redirect('Home:Home')
        return render (request, 'Blog/editar_blog_formulario.html', {"form": miFormulario})
    else:

        miFormulario = FormularioBlog (initial={
            "titulo": blog.titulo,
            "descripcion": blog.descripcion,
            "autor": blog.autor,
            "categoria":blog.categoria
            })
        return render (request, 'Blog/editar_blog_formulario.html', {"form": miFormulario,"id":blog.id}) # type: ignore
    
####VISTAS BASADAS EN CLASES####

class BlogList(ListView):
    
    model= Blog
    template_name= 'Blog/blog_list.html'
    context_object_name='blogs'

class BlogDetail(DetailView):
    model= Blog
    template_name='Blog/blog_detail_vbc.html'
    context_object_name='blog'

class BlogCreate(CreateView):
    model= Blog
    template_name='Blog/crear_blog_formulario.html'
    fields= ["titulo", "descripcion", "autor", "categoria"]
    success_url= '/buscar_blogs_todos/'

class BlogUpdate(UpdateView):
    model= Blog
    template = 'Blog/blod_update_vbc.html'
    fields=["titulo", "contenido", "autor", "categoria"]
    success_url= '/buscar_blogs_todos/'

class BlogDelete(UpdateView):
    model= Blog
    template = 'Blog/blod_delete_vbc.html'
    success_url= '/buscar_blogs_todos/'