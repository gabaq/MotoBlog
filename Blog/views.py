from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from Blog.models import *
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required



""" from Blog.forms import * """


# Create your views here.

def inicio2(request):
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'content.html')

def about(request):
    return render(request, 'about.html')

def pages(request):
    return render(request, 'pages.html')




def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            subtitulo = form.cleaned_data['subtitulo']
            cuerpo = form.cleaned_data['cuerpo']
            autor = form.cleaned_data['autor']
            fecha = form.cleaned_data['fecha']
            imagen = form.cleaned_data['imagen']

            post = Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.titulo = form.cleaned_data['titulo']
            post.subtitulo = form.cleaned_data['subtitulo']
            post.cuerpo = form.cleaned_data['cuerpo']
            post.autor = form.cleaned_data['autor']
            post.fecha = form.cleaned_data['fecha']
            post.imagen = form.cleaned_data['imagen']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(initial={
            'titulo': post.titulo,
            'subtitulo': post.subtitulo,
            'cuerpo': post.cuerpo,
            'autor': post.autor,
            'fecha': post.fecha,
            'imagen': post.imagen,
        })
    
    return render(request, 'post_update.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})