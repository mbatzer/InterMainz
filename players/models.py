from django.db import models


class Player(models.Model):
    possible_positions = (
        ('portero', 'Portero'),
        ('defensa', 'Defensa'),
        ('centrocampo', 'Centrocampista'),
        ('delantero', 'Delantero')
    )
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=possible_positions)
    jersey_number = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    picture = models.ImageField(default="default.jpg", upload_to="player_pics")

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
