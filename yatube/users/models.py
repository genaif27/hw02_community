from django.db import models
from django.core.validators import MinValueValidator

class New_User(models.Model):
    first_name = models.CharField(max_length=200)   # Название
    last_name = models.CharField(max_length=100)   # Индекс издания
    quality = models.CharField(max_length=100)
    # pages = models.IntegerField(              
        # validators=[MinValueValidator(1)]
    # )   