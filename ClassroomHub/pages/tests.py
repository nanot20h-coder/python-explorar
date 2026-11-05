
from django.test import TestCase
from django.urls import reverse


class PagesTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("pages:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "ClassroomHub es un portal educativo"
        )

    def test_resources_page(self):
        response = self.client.get(reverse("pages:resources"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python basics")
        self.assertContains(response, "Git and GitHub")
        self.assertContains(response, "Available")
        self.assertContains(response, "Coming soon")

    def test_about_page(self):
        response = self.client.get(reverse("pages:about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Practice URL routing, views, and templates."
        )

    def test_pages_use_base_template(self):
        pages = [
            "pages:home",
            "pages:resources",
            "pages:about",
        ]

        for page in pages:
            response = self.client.get(reverse(page))
            self.assertTemplateUsed(response, "pages/base.html")

    def test_unknown_page_returns_404(self):
        response = self.client.get("/pagina-inventada/")

        self.assertEqual(response.status_code, 404)
