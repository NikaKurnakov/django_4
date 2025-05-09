import folium
import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils import timezone


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = timezone.localtime(timezone.now())
    active_entities = PokemonEntity.objects.filter(
        appeared_at__lte=now,
        disappeared_at__gte=now
    ).select_related('pokemon')
    unique_pokemons = {entity.pokemon for entity in active_entities}
    pokemons_on_page = []
    for pokemon in unique_pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else None,
            'title_ru': pokemon.title,
        })
    map_pokemons = []
    for entity in active_entities:
        map_pokemons.append({
            'lat': entity.lat,
            'lon': entity.lon,
            'img_url': request.build_absolute_uri(entity.pokemon.image.url) if entity.pokemon.image else None,
            'pokemon_id': entity.pokemon.id,
            'level': entity.level,
            'health': entity.health,
            'strength': entity.strength,
            'defence': entity.defence,
            'stamina': entity.stamina,
        })

    return render(request, "mainpage.html", context={
        'pokemons': pokemons_on_page,
        'map_pokemons': map_pokemons,
    })


def show_pokemon(request, pokemon_id):
    current_time = timezone.localtime(timezone.now())
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)


    pokemon_data = {
        'pokemon_id': pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.image.url) if pokemon.image else None,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'previous_evolution': pokemon.previous_evolution,
        'next_evolution': pokemon.next_evolutions.first(),
    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data,
        'current_time': current_time.strftime("%Y-%m-%d %H:%M:%S"),
    })
