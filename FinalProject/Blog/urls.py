
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #PATH CRUD
    path ('Blogs/', views.Blogs, name='Blogs'), #type:ignore
    path ('crear_blog/', views.crear_blog, name='crear_blog'), #type:ignore
    path ('buscar_blog/', views.buscar_blog, name='buscar_blog'), #type:ignore
    path ('crear_comentario/', views.crear_comentario, name='crear_comentario'), #type:ignore
    path ('buscar_comentario/', views.buscar_comentario, name='buscar_comentario'), #type:ignore
    path ('buscar_blogs_todos/', views.buscar_blog_todos, name='buscar_blogs_todos'),
    path ('eliminar_blog/<int:id>', views.eliminar_blog, name='eliminar_blog'), #type:ignore
    #PATH VISTAS BASADAS EN CLASE
    path ('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path ('blog_detail/<pk>', views.BlogDetail.as_view(), name='blog_detail'),
    path ('blog_create/', views.BlogCreate.as_view(), name='blog_create'),
    path ('blog_update/<pk>', views.BlogUpdate.as_view(), name='blog_update'),
    path ('blog_delete/<pk>', views.BlogDelete.as_view(), name='blog_delete'),
]
