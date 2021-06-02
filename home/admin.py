from django.contrib import admin
from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')


admin.site.register(Movies, MoviesAdmin)
