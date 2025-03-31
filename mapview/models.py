from django.contrib.gis.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.name

class NIHCenter(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField()

    def __str__(self):
        return self.name
