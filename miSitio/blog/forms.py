from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'shortext','text','imagenPortada','imagen1','imagen2','imagen3','imagenfondo','gameForWindows')
        labels={
            'title':'Titulo del Juego*',
            'text':'Descripcion General*',
            'shortext':'Descripción Corta',
            'imagenPortada':'Imagen de Portada',
            'imagen1':'Imagen Principal ',
            'imagen2': 'ScreenShoot n°1',
            'imagen3': 'ScreenShoot n°2',
            'imagenfondo': 'Imagen de Fondo de la pagina',
            'gameForWindows':'Juego'

        }
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
