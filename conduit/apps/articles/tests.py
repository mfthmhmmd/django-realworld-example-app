import unittest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from conduit.apps.authentication.models import User


class ArticleTestCase(APITestCase):
    def setUp(self):
        user, _ = User.objects.get_or_create(
            defaults={"username": "usertest", "email": "test@test.com"}
        )
        self.client.credentials(HTTP_AUTHORIZATION="Token " + user.token)

    def test_create_new_article(self):
        url = reverse("articles:article-list")
        data = {
            "article": {
                "slug": "how-to-train-your-dragon",
                "title": "How to train your dragon",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
            }
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


if __name__ == "__main__":
    unittest.main()
