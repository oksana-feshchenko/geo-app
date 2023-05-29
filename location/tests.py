from django.contrib.gis.geos import GEOSGeometry
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from location.models import Place


class PlaceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.place = Place.objects.create(
            name="Place 1", description="Description 1", geom="POINT(0 0)"
        )

    def test_create_place(self):
        # Test creating a new place via the API
        data = {
            "name": "New Place",
            "description": "New Description",
            "geom": "POINT(1 1)",
        }

        url = reverse("location:place-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Place.objects.filter(name="New Place").exists())

    def test_get_place(self):
        # Test retrieving a place via the API
        url = reverse("location:place-detail", kwargs={"pk": self.place.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.place.id)
        self.assertEqual(response.data["name"], self.place.name)
        self.assertEqual(response.data["description"], self.place.description)
        self.assertEqual(
            GEOSGeometry(response.data["geom"]).wkt, self.place.geom.wkt
        )

    def test_update_place(self):
        # Test updating a place via the API

        data = {
            "name": "Updated Place",
            "description": "Updated Description",
            "geom": "POINT(2 2)",
        }

        url = reverse("location:place-detail", kwargs={"pk": self.place.pk})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.place.refresh_from_db()
        self.assertEqual(self.place.name, "Updated Place")
        self.assertEqual(self.place.description, "Updated Description")
        self.assertEqual(self.place.geom.wkt, "POINT (2 2)")

    def test_partial_update_place(self):
        data = {
            "description": "Updated Description",
        }
        url = reverse("location:place-detail", kwargs={"pk": self.place.pk})
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.place.refresh_from_db()
        self.assertEqual(self.place.description, "Updated Description")

    def test_delete_place(self):
        # Test deleting a place via the API
        url = reverse("location:place-detail", kwargs={"pk": self.place.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Place.objects.filter(pk=self.place.pk).exists())


class ClosestPlaceTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_closest_place(self):
        Place.objects.create(
            name="Place 1", description="Description 1", geom="POINT(0 0)"
        )
        Place.objects.create(
            name="Place 2", description="Description 2", geom="POINT(1 1)"
        )
        # Test getting the closest place via the API view
        longitude = 2.0
        latitude = 2.0
        expected_place = Place.objects.create(
            name="Closest Place",
            description="Closest Place Description",
            geom="POINT(2 2)",
        )
        url = reverse("location:closest-place")
        response = self.client.get(url, {"long": longitude, "lat": latitude})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], expected_place.id)
        self.assertEqual(response.data["name"], expected_place.name)
        self.assertEqual(
            response.data["description"], expected_place.description
        )
        self.assertEqual(
            GEOSGeometry(response.data["geom"]).wkt, expected_place.geom.wkt
        )

    def test_get_closest_place_no_places(self):
        # Test getting the closest place when no places exist
        url = reverse("location:closest-place")
        response = self.client.get(url, {"long": 2.0, "lat": 2.0})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["message"], "No places found.")
