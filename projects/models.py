from django.db import models

class Anime(models.Model):
    titulo = models.CharField(max_length=255)
    tipo_anime = models.CharField(max_length=50, default='Desconocido')
    episodios = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(max_length=500)
    fecha = models.PositiveIntegerField(null=True, blank=True)
    estado = models.CharField(max_length=50, default='Finalizado')
    generos = models.TextField()
    sinopsis = models.TextField(default='Sin sinopsis disponible.')

    def __str__(self):
        return self.titulo
