from django.test import TestCase
from .models import Item
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        self.post = Item.objects.create(
            name="Test Post",
            description="This is a test post",
        )

        def test_post_creation(self):
            post = Item.objects.get(id=1)
            self.assertEqual(post.name, "Test Post")
            self.assertEqual(post.description, "This is a test post")

        def test_post_created_auto_now_add(self):
            post = Item.objects.get(id=1)
            self.assertIsNotNone(post.created_at)