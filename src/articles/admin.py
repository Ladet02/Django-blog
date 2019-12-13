from django.contrib import admin

# Register your models here.
from .models import Author, Category, Article, Tag, Comment

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'timestamp', 'author', 'categories', 'tags')
    list_per_page = 20

    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'content', 'user')
    search_fields = ('article', 'content', 'user')
    list_per_page = 20


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
