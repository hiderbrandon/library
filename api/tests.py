from django.test import TestCase
from django.urls import reverse # new
from rest_framework import status # new
from rest_framework.test import APITestCase
# new
from book.models import Book
class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Berserk",
            subtitle="Berserk the lost children",
            author="kentarou miura",
            isbn="123456789",
        )


def test_api_listview(self):
    response = self.client.get(reverse("book_list"))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(Book.objects.count(), 1)
    self.assertContains(response, self.book)


def test_api_detailview(self):
    response = self.client.get(reverse("book_detail", kwargs={"pk": self.book.id}),format="json")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(Book.objects.count(), 1)
    self.assertContains(response, "First book")
