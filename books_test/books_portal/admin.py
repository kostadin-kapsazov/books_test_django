

from django.contrib import admin

from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'pages')

admin.site.register(Books, BooksAdmin)


