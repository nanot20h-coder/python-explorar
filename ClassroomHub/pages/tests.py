
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import ProtectedError
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

    def test_category_cannot_be_deleted_with_resources(self):
        Resource.objects.create(
            title="Recurso protegido",
            description="Prueba de protección",
            category=self.category
        )

        with self.assertRaises(ProtectedError):
            self.category.delete()

        self.assertTrue(
            Category.objects.filter(pk=self.category.pk).exists()
        )


class AuthenticationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="TestPassword2026!"
        )

    def test_signup_page_loads(self):
        response = self.client.get(reverse("pages:signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_creates_user(self):
        response = self.client.post(
            reverse("pages:signup"),
            {
                "username": "newuser",
                "password1": "StrongPassword2026!",
                "password2": "StrongPassword2026!",
            },
        )
        self.assertRedirects(response, reverse("pages:login"))
        self.assertTrue(
            get_user_model().objects.filter(username="newuser").exists()
        )

    def test_signup_rejects_existing_username(self):
        response = self.client.post(
            reverse("pages:signup"),
            {
                "username": "testuser",
                "password1": "StrongPassword2026!",
                "password2": "StrongPassword2026!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            get_user_model().objects.filter(username="testuser").count(),
            1,
        )

    def test_login_page_loads(self):
        response = self.client.get(reverse("pages:login"))
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        response = self.client.post(
            reverse("pages:login"),
            {
                "username": "testuser",
                "password": "TestPassword2026!",
            },
        )
        self.assertRedirects(response, reverse("pages:dashboard"))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(
            reverse("pages:login"),
            {
                "username": "testuser",
                "password": "incorrect",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("pages:dashboard"))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_displays_username(self):
        self.client.login(
            username="testuser",
            password="TestPassword2026!",
        )
        response = self.client.get(reverse("pages:dashboard"))
        self.assertContains(response, "testuser")

    def test_dashboard_session_counter_increases(self):
        self.client.login(
            username="testuser",
            password="TestPassword2026!",
        )
        first = self.client.get(reverse("pages:dashboard"))
        second = self.client.get(reverse("pages:dashboard"))

        self.assertEqual(first.context["visit_count"], 1)
        self.assertEqual(second.context["visit_count"], 2)

    def test_logout_post_ends_session(self):
        self.client.login(
            username="testuser",
            password="TestPassword2026!",
        )
        response = self.client.post(reverse("pages:logout"))
        self.assertRedirects(response, reverse("pages:home"))

    def test_logout_get_is_not_allowed(self):
        self.client.login(
            username="testuser",
            password="TestPassword2026!",
        )
        response = self.client.get(reverse("pages:logout"))
        self.assertEqual(response.status_code, 405)

    def test_authenticated_user_cannot_signup_again(self):
        self.client.login(
            username="testuser",
            password="TestPassword2026!",
        )
        response = self.client.get(reverse("pages:signup"))
        self.assertRedirects(response, reverse("pages:dashboard"))


class ResourceReviewPermissionTests(TestCase):

    def setUp(self):
        self.client = Client()
        User = get_user_model()

        self.reviewer = User.objects.create_user(
            username="reviewer",
            password="ReviewerPassword2026!",
        )

        self.regular_user = User.objects.create_user(
            username="regular",
            password="RegularPassword2026!",
        )

        content_type = ContentType.objects.get_for_model(Resource)
        permission = Permission.objects.get(
            content_type=content_type,
            codename="view_resource",
        )

        self.group = Group.objects.create(name="Catalog reviewers")
        self.group.permissions.add(permission)
        self.reviewer.groups.add(self.group)

    def test_reviewer_can_open_review(self):
        self.client.login(
            username="reviewer",
            password="ReviewerPassword2026!",
        )
        response = self.client.get(reverse("pages:resource-review"))
        self.assertEqual(response.status_code, 200)

    def test_regular_user_cannot_open_review(self):
        self.client.login(
            username="regular",
            password="RegularPassword2026!",
        )
        response = self.client.get(reverse("pages:resource-review"))
        self.assertEqual(response.status_code, 403)

    def test_anonymous_user_is_redirected_from_review(self):
        response = self.client.get(reverse("pages:resource-review"))
        self.assertEqual(response.status_code, 302)

    def test_reviewer_has_view_permission(self):
        self.assertTrue(
            self.reviewer.has_perm("pages.view_resource")
        )

    def test_regular_user_does_not_have_view_permission(self):
        self.assertFalse(
            self.regular_user.has_perm("pages.view_resource")
        )

    def test_resource_catalog_is_public(self):
        response = self.client.get(reverse("pages:resources"))
        self.assertEqual(response.status_code, 200)


