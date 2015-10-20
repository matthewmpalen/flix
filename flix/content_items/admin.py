# Django
from django.contrib import admin

# Local
from .models import Person, Movie, Series, Episode

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at', 'updated_at')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'us_release_date', 'mpaa_rating', 
        'created_at', 'updated_at')

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'us_release_date', 
        'us_tv_parental_rating', 'created_at', 'updated_at')
    list_filter = ('us_tv_parental_rating',)

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('series', 'title', 'description', 'created_at', 
        'updated_at')
    list_filter = ('series',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Episode, EpisodeAdmin)
