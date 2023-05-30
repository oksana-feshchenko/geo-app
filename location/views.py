from django.contrib.gis.geos import Point
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from django.contrib.gis.db.models.functions import Distance
from rest_framework.response import Response
from rest_framework.views import APIView


from location.models import Place
from location.serilalizers import PlaceSerializer, PlaceListDetailSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return PlaceListDetailSerializer
        return PlaceSerializer


class ClosestPlaceAPIView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="long",
                type=float,
                location=OpenApiParameter.QUERY,
                description="The longitude of the target location.{ex. ?lon=20.1}",
            ),
            OpenApiParameter(
                name="lat",
                type=float,
                location=OpenApiParameter.QUERY,
                description="The latitude of the target location.{ex. ?lat=50.1234}",
            ),
        ],
        responses={200: PlaceSerializer(), 404: "No places found."},
    )
    def get(self, request):
        longitude = float(self.request.query_params.get("long"))
        latitude = float(self.request.query_params.get("lat"))
        point = Point(longitude, latitude, srid=4326)

        closest_place = (
            Place.objects.annotate(distance=Distance("geom", point))
            .order_by("distance")
            .first()
        )

        if closest_place:
            serializer = PlaceSerializer(closest_place)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "No places found."},
                status=status.HTTP_404_NOT_FOUND,
            )
