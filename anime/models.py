from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    bc_year = models.IntegerField(
        default=timezone.now().year,
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(3000)
        ]
    )
    synopsis = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Story(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100)
    bc_date = models.DateField('broadcast date')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.subtitle
