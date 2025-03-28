from django.utils.html import format_html
from django.contrib import admin
from .models import Genra, Movie


class GenraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('id', 'title', 'release_year',
                    'number_in_stock', 'daily_rate', 'genre', 'image_display')

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
        return "No Image"

    image_display.allow_tags = True
    image_display.short_description = 'Preview'


admin.site.register(Genra, GenraAdmin)
admin.site.register(Movie, MovieAdmin)
