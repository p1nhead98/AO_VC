from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    shortext = models.TextField(max_length=50, blank=True,null=True)
    imagenPortada = models.ImageField(upload_to='images/',blank=True, null=True)
    imagen1 = models.ImageField(upload_to='images/',blank=True, null=True)
    imagen2 = models.ImageField(upload_to='images/',blank=True,  null=True)
    imagen3 = models.ImageField(upload_to='images/',blank=True,  null=True)
    imagenfondo = models.ImageField(upload_to='images/', blank=True, null= True)
    gameForWindows = models.FileField(upload_to='games/', blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
