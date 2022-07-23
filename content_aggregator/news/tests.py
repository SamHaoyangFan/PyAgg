"""
from django.test import TestCase
from django.utils import timezone
from .models import Post
from django.urls.base import reverse
from datetime import datetime
# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.posts = Post.objects.create(
            title="My Post",
            description="Look, I made it!",
            pubdate=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            p_title="My New Post"
        )

    def test_post_content(self):
        self.assertEqual(self.posts.description, "Look, I made it!")
        self.assertEqual(self.posts.link, "https://myawesomeshow.com")


    def test_post_str_representation(self):
        self.assertEqual(
            str(self.posts), "My New Post: My Post"
        )

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "My Post")
"""
