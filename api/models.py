from django.db import models


class Superhero(models.Model):
    name = models.CharField(max_length=60, unique=True)
    alter_ego = models.CharField(max_length=60)
    universe = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
