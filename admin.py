from django.contrib import admin
from .models import Pokemon, PokemonEntity


admin.site.register(Pokemon)
admin.site.register(PokemonEntity)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'lat', 'lon', 'appeared_at', 'disappeared_at')
    list_filter = ('pokemon', 'appeared_at')
    search_fields = ('pokemon__title',)
    fieldsets = (
        (None, {
            'fields': ('pokemon', ('lat', 'lon'))
        }),
        ('Временные параметры', {
            'fields': ('appeared_at', 'disappeared_at'),
            'classes': ('collapse',)
        }),
    )
