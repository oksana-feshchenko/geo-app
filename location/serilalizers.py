from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from location.models import Place


class PlaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Place
        geo_field = "geom"
        fields = ("id", "name", "description", "geom")


class PlaceListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("id", "name", "description", "geom")
