from django.contrib import admin
from .models import Pokemon, PokemonEntity


admin.site.register(Pokemon)
admin.site.register(PokemonEntity)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'lat', 'lon')
    list_filter = ('pokemon',)
    search_fields = ('pokemon__title',)
