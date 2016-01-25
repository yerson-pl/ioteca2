from django.contrib import admin
from catalogo.models import Categoria

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "estado")
    search_fields = ("nombre", "codigo",)
    list_per_page = 3

admin.site.register(Categoria, CategoriaAdmin)
