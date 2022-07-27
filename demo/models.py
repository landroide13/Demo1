from django.db import models

# Create your models here.

class Book(models.Model):
    GENRE = (
        ('SF', 'Sci-fi'),
        ('DR', 'Drama'),
        ('HO', 'Horror'),
        ('UN', 'Unknown')
    )
    title = models.CharField(max_length=100, blank=False, unique=True)
    genre = models.CharField(max_length=55, choices=GENRE, default='UN')
    description = models.TextField(max_length=250,blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    is_published = models.BooleanField(default=False)
    published = models.DateField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='covers/', blank=True)









