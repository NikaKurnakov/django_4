from django.contrib import admin
from .models import Pokemon, PokemonEntity


admin.site.register(Pokemon)
admin.site.register(PokemonEntity)


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en', 'title_jp')
    search_fields = ('title', 'title_en', 'title_jp')
    fieldsets = (
        (None, {
            'fields': ('title', 'title_en', 'title_jp', 'image', 'description')
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
