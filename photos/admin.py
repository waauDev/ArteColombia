from django.contrib import admin

# Register your models here.


from .models import Photo, Category, Autor, Museo, Tecnica

admin.site.register(Category)

admin.site.register(Photo)

admin.site.register(Autor)

admin.site.register(Museo)

admin.site.register(Tecnica)