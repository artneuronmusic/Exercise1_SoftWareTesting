from unittest import TestCase
from blog import Blog

class TestBlog(TestCase):

    def test_call_blog(self):
        b = Blog("Love", "Kingsman")
        b.posts = []

        self.assertEqual("Love", b.title )
        self.assertEqual("Kingsman", b.author)
        self.assertEqual([], b.posts)
        self.assertEqual("Love by Kingsman (0 posts)", b.__repr__())

    def test_posts(self):
        b = Blog("Love", "Kingsman")
        b.posts = ["Published by Yale Univ."]
        b2 = Blog("Star", "Wineman")
        b2.posts = ["Published by Standford Univ", "Published by Rice Univ"]

        self.assertEqual("Love by Kingsman (1 post)", b.__repr__())
        self.assertEqual("Star by Wineman (2 posts)", b2.__repr__())


    def test_create_post(self):
        b = Blog("Love", "Kingsman")
        b.create_post("love", "siblings")

        self.assertEqual(b.posts[0].name, "love")
        self.assertEqual(b.posts[0].content, "siblings")

    def test_no_json(self):
        b = Blog("Love", "Kingsman")
        expected = {"title": "Love", "author": "Kingsman", "posts": []}

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog("Love", "Kingsman")
        b.create_post("love", "siblings")
        expected = {"title": "Love", "author": "Kingsman",
                    "posts": [{"title":"love", "content":"siblings"}]}

        self.assertDictEqual(expected, b.json())






