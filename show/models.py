from django.db import models


class ShowPicture(models.Model):
    # picture = models.ImageField(default=".jpg", upload_to="carousel")
    LEFT = 'lf'
    CENTRE = 'ct'
    RIGHT = 'rg'
    possible_locations = (
        (LEFT, 'left'),
        (CENTRE, 'centre'),
        (RIGHT, 'right')
    )
    location = models.CharField(max_length=2, choices=possible_locations, default=CENTRE)
    picture = models.ImageField(upload_to="carousel")
