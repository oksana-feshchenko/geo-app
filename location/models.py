from django.contrib.gis.db import models
# База даних має містити таблицю
# places , яка включає поля id (primary key), name (назва місця), description (опис
# місця) і geom (POINT geometry type) для координат місця.


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    geom = models.PointField()

    def __str__(self):
        return f"{self.name}({self.geom})"
