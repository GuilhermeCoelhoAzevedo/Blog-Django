from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Post(models.Model):
    categoria = models.ForeignKey(
        'Categoria',
        null=True,
        on_delete=models.SET_NULL,
    )

    titulo = models.CharField(
        max_length=100
    )

    url = models.SlugField(
        max_length=100,
        unique=True
    )

    preview = models.TextField(
        max_length=400
    )

    corpo = RichTextUploadingField(config_name='special', external_plugin_resources=[('youtube', '/static/ckeditor/ckeditor/plugins/youtube/youtube/','plugin.js')],)

    autor = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    imagem = models.ImageField(
        upload_to='uploads',
        blank=True,
        null=True
    )

    data = models.DateField(
        db_index=True,
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo

    def getImagem(self):
        return settings.MEDIA_URL + str(self.imagem)


class Categoria(models.Model):
    titulo = models.CharField(
        max_length=100,
        db_index=True
    )

    url = models.SlugField(
        max_length=100,
        db_index=True
    )

    def __str__(self):
        return self.titulo
