from django.test import TestCase

from joins.models import Join


class ShareViewTests(TestCase):
    def test_share_view_renders_for_known_ref_id(self):
        join = Join.objects.create(
            email="owner@example.com",
            ref_id="abc123def4",
            ip_address="127.0.0.1",
        )
        Join.objects.create(
            email="friend1@example.com",
            ref_id="friend0001",
            ip_address="127.0.0.1",
            friend=join,
        )
        Join.objects.create(
            email="friend2@example.com",
            ref_id="friend0002",
            ip_address="127.0.0.1",
            friend=join,
        )

        response = self.client.get(f"/{join.ref_id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["count"], 2)
        self.assertEqual(
            response.context["ref_url"],
            "http://127.0.0.1:8000/?ref=abc123def4",
        )

    def test_share_view_404s_for_unknown_ref_id(self):
        response = self.client.get("/doesnotexist")

        self.assertEqual(response.status_code, 404)
