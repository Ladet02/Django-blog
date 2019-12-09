from django.contrib import admin

# Register your models here.
from .models import Author, Category, Article

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article)
