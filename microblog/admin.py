from django.contrib import admin
from microblog.models import Post, Categoria

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data',)
    ordering = ('data', 'titulo', 'categoria',)
    search_fields = ('titulo', 'categoria', 'data',)

@admin.register(Categoria)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo','url',)
    ordering = ('titulo','url',)
    search_fields = ('titulo','url',)