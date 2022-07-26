from django.contrib import admin
from .models import Book

# Register your models here.

#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'genre', 'description', 'price', 'is_published','published', 'cover']
    list_display = ['title', 'description', 'price']
    list_filter= ['genre']
    search_fields = ['title']

