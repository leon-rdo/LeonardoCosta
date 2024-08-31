from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Nome", max_length=100, unique=True)
    description = models.TextField("Descrição", blank=True, null=True)
    slug = models.SlugField("Slug", max_length=100, unique=True)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("Nome", max_length=50, unique=True)
    slug = models.SlugField("Slug", max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", max_length=200, unique=True)
    headline = models.CharField("Manchete", max_length=200)
    content = CKEditor5Field("Conteúdo", config_name='extends')
    cover_image = models.ImageField("Imagem de Capa", upload_to='posts/covers/', blank=True, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', verbose_name='Autor')
    categories = models.ManyToManyField(Category, related_name='posts', verbose_name='Categorias')
    tags = models.ManyToManyField(Tag, related_name='posts', verbose_name='Tags')
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    published_at = models.DateTimeField("Publicado em", blank=True, null=True)
    is_published = models.BooleanField("Está publicado?", default=False)
    views = models.PositiveIntegerField("Vizualizações", default=0, editable=False)

    def __str__(self):
        return self.title
    
    def save(self):
        if self.is_published and not self.published_at:
            self.published_at = datetime.now()
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
