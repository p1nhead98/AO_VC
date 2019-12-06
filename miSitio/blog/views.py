from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.views import LoginView
from django.utils import timezone
from django.forms import Form,CharField,PasswordInput
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
from django.db.models import Q
from .forms import PostForm, RegisterForm
from django.db import models
# Create your views here.


#Metodo para ver los proyectos creados en la pagina
def post_list(request):
    #post ordenados por fecha de publicacion
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


#Metodo para ver los proyectos creados por ti
def post_profile(request):
    #post ordenados por fecha de publicacion
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_profile.html', {'posts':posts})

#Metodo para mostrar datos en profundidad de los proyectos ingresados en la pagina
def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#Metodo para ingresar un nuevo proyecto a la pagina
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            #Se establece que el nombre del autor es el username del usuario que inicio sesion
            post.author = request.user
            #Se establece que la fecha de publicacion es la fecha/hora actual 
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


    

        

#Metodo para editar un proyecto de la pagina
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #Se valida si el usuario que inicio sesion es dueño del proyecto, comparando el nombre de usuario logeado con el usuario que creo el proyecto
    if post.author == request.user or request.user.is_staff:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post) 
    #Si este no es dueño del post, sera redirigido a la pagina anterior
    else:
        return redirect('post_detail',pk=post.pk)
    return render(request, 'blog/post_edit.html', {'form': form})

#Metodo para eliminar un proyecto 
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete.html',{'post':post})

#Metodo para el registro de usuarios
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = RegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            #Se definen los campos que tendra el form
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            do_login(request, user) 
            return redirect('/')
    else:
        form = RegisterForm()
    #Se elimina informacion innecesaria en la pantalla
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "blog/register.html", {'form':form})

#Metodo para el login de usuarios

def login(request): 
    form=AuthenticationForm()
    if request.method=="POST":
        form =LoginForm(data=request.POST)
        if form.is_valid():
            #Campos del form del login
            username  = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None: 
                do_login(request,user)
                return redirect('post_list')
    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form':form})

#metodo para retornar datos del user que inicio sesion
def userquery(request):
    users=request.user
    return render(request, 'blog/profile.html', {'user':User})

