try:
    from django.contrib.gis.db import models as _models
    GIS_AVAILABLE = True
except Exception:
    from django.db import models as _models
    GIS_AVAILABLE = False

models = _models

if not GIS_AVAILABLE:
    class MultiPolygonField(models.JSONField):
        pass

    class PointField(models.JSONField):
        pass
else:
    MultiPolygonField = models.MultiPolygonField
    PointField = models.PointField

class State(models.Model):
    name = models.CharField(max_length=100)
    geom = MultiPolygonField()

    def __str__(self):
        return self.name

class NIHCenter(models.Model):
    name = models.CharField(max_length=100)
    geom = PointField()

    def __str__(self):
        return self.name
