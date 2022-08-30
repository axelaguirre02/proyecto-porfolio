from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='posts/images')
    date = models.DateField(auto_now_add=True)

    class Meta:
        
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.title

