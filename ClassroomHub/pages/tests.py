
from django.test import TestCase
from django.urls import reverse
from .models import Category, Resource


class PagesTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("pages:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "ClassroomHub es un portal educativo"
        )

    def test_resources_page(self):
        category = Category.objects.create(
            name="Programación"
        )

        Resource.objects.create(
            title="Python basics",
            description="Introduction to Python.",
            category=category,
            available=True
        )

        Resource.objects.create(
            title="Git and GitHub",
            description="Introduction to version control.",
            category=category,
            available=False
        )

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

    def test_resources_empty_state(self):
        response = self.client.get(reverse("pages:resources"))

        self.assertContains(response, "No resources are available.")

        
class ModelsTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Diseño web",
            description="Recursos de diseño web."
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Diseño web")

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Diseño web")

    def test_resource_creation(self):
        resource = Resource.objects.create(
            title="HTML básico",
            category=self.category
        )

        self.assertEqual(resource.title, "HTML básico")

    def test_resource_string_representation(self):
        resource = Resource.objects.create(
            title="CSS básico",
            category=self.category
        )

        self.assertEqual(str(resource), "CSS básico")

    def test_resource_default_availability(self):
        resource = Resource.objects.create(
            title="JavaScript básico",
            category=self.category
        )

        self.assertTrue(resource.available)
