from django.contrib import admin
from .models import Pokemon, PokemonEntity


admin.site.register(Pokemon)
admin.site.register(PokemonEntity)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title', 'previous_evolution')
    list_filter = ('previous_evolution',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'title_en', 'title_jp', 'image', 'description')
        }),
        ('Эволюция', {
            'fields': ('previous_evolution',),
            'classes': ('collapse',)
        }),
    )

class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = ('pokemon', 'level', 'health', 'strength', 'defence', 'stamina', 'is_active')
    list_filter = ('pokemon', 'level')
    search_fields = ('pokemon__title',)
    fieldsets = (
        ('Основное', {
            'fields': ('pokemon', ('lat', 'lon'))
        }),
        ('Время', {
            'fields': ('appeared_at', 'disappeared_at'),
            'classes': ('collapse',)
        }),
        ('Характеристики', {
            'fields': (
                ('level', 'health'),
                ('strength', 'defence'),
                ('stamina',)
            )
        }),
    )
