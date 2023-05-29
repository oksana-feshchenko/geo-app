from django.contrib import admin
from django.contrib.gis import admin as geo_admin
from .models import Place


@admin.register(Place)
class PlaceAdmin(geo_admin.OSMGeoAdmin):
    list_display = ("id", "name", "description", "geom")
    search_fields = ("name",)
