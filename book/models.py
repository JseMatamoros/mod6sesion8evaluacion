from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )
    
    def __str__(self):
        return self.titulo