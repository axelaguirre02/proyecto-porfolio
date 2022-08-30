from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='projects/images/')
    url = models.URLField(blank=True)

    class Meta:
        
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.title

