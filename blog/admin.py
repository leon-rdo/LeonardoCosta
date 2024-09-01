from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published_at')
    list_filter = ('is_published', 'published_at', 'author')
    search_fields = ('title', 'headline')
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories', 'tags')
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, 'Publicações publicadas com sucesso.')

    publish.short_description = 'Publicar publicações selecionadas'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
