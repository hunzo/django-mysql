from .models import Post
from django.test import TestCase

class PostTestCase(TestCase):
    def testPost(self):
        post = Post(author="admin", title="my title", content="myContent")
        self.assertEqual(post.author, "admin")
        self.assertEqual(post.title, "my titile")
        self.assertEqual(post.content, "myContent")