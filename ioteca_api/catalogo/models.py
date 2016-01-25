from django.db import models


# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=60, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta(object):
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre
