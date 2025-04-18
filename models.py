from django.db import models
from django.core.validators import MinValueValidator


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images', null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Время появления', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', null=True, blank=True)
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True, validators=[MinValueValidator(1)])
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True, validators=[MinValueValidator(1)])
    strength = models.IntegerField(verbose_name='Атака', null=True, blank=True, validators=[MinValueValidator(1)])
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True, validators=[MinValueValidator(1)])
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.pokemon.title} (уровень {self.level or '?'})"
