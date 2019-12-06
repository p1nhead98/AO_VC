from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Post
from django.forms import PasswordInput,TextInput
from django.core.exceptions import ValidationError

#formulario del ingreso y edit de posts
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'shortext','text','imagenPortada','imagen1','imagen2','imagen3','imagenfondo','gameForWindows')
       #Titulos para los campos del formulario
        labels={
            'title':'Titulo del Juego*',
            'text':'Descripcion General*',
            'shortext':'Descripción Corta',
            'imagenPortada':'Imagen de Portada',
            'imagen1':'Imagen Principal ',
            'imagen2': 'ScreenShoot n°1',
            'imagen3': 'ScreenShoot n°2',
            'imagenfondo': 'Imagen de Fondo de la pagina',
            'gameForWindows':'Juego*'

        }
        #Widgets para personalizar el aspectos de los campos del formulario
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresar titulo del proyecto..'}),
            'imagenPortada':forms.FileInput(attrs={'class':'form-control'}),
            'imagen1':forms.FileInput(attrs={'class':'form-control'}),
            'imagen2':forms.FileInput(attrs={'class':'form-control'}),
            'imagen3':forms.FileInput(attrs={'class':'form-control'}),
            'imagenfondo':forms.FileInput(attrs={'class':'form-control'}),
            'gameForWindows':forms.FileInput(attrs={'class':'form-control'}),
            'shortext':forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese una descripcion de a lo mas 50 caracteres...','rows':'1'}),
            'text':forms.Textarea(attrs={'class':'form-control', 'rows':'3','placeholder':'Ingrese una descripcion general del proyecto...'})
        }

#Creacion de formulario para el registro de usuarios
class RegisterForm(UserCreationForm):
    
    #Metodo para Personalizar la forma de los campos de password en el form, no se porque no se puede en los widgets
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
        self.fields['email'].required=True
        self.fields['email'].unique=True
        self.fields['username'].unique=True

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email ya se encuentra registrado")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este Username ya se encuentra registrado")
        return self.cleaned_data
  
    class Meta:
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        #Personalizacion de campos del formulario
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de usuario'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Campo no obligatorio'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Campo no obligatorio'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese Direccion email'}),
            
           
        }

#Form para el login de usuario, AuthenticationForm define que el formulario es para la identificacion de un usuario
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            #Se definen los widgets para ambas columnas
            self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Ingrese contraseña', 'class': 'form-control'})
            self.fields['username'].widget = TextInput(attrs={'placeholder':'Ingrese Username', 'class':'form-control'})
    class Meta:
        model=User
        fields=('username','password')




