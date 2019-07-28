from unittest import TestCase
import app
from unittest.mock import patch
from blog import Blog
from post import Post

class AppTest(TestCase):

    def test_prompt(self):
        with patch("builtins.input", return_value="q") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
        #set return_value to q, then the while loop will not do infinitely loop.


    def test_menu_print_blogs(self):
        with patch("application.print_blogs", return_value="q") as mocked_print_blogs:
            with patch("builtins.input", return_value="q") as mocked_input:
                app.menu()
                mocked_print_blogs.assert_called()
                #when u patch a function, using assert_called()



    def test_print_blogs(self):

        blog = Blog("Love", "Kingsman")
        app.blogs = dict({"title": blog})

        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Love by Kingsman (0 posts)")
            self.assertIsNotNone(app.blogs.items())


    def test_create_blog(self):
        with patch("builtins.print") as mocked_print:
            with patch("builtins.input") as mocked_input:
                mocked_input.side_effect = ("Automation", "Alan")
                app.create_blog()
                self.assertIsNotNone(app.blogs.get("Automation"))
                self.assertIsNotNone(app.blogs)
                #mocked_print.assert_called_with(application.blogs["Automation"])



    def test_read_blog(self):
        blog = Blog("Love", "Kingsman")
        app.blogs = dict({"Love": blog})
        with patch("builtins.input", return_value="Love") as mocked_input:
            #application.read_blog()
            #self.assertIsNotNone(application.blogs.get("Love"))

            with patch("application.print_posts") as mocked_print_posts:
                app.read_blog()
                mocked_print_posts.assert_called_with(blog)
        #this one, so far, is the trickist one;


    def test_print_posts(self):
        blog = Blog("automation", "Clark")
        blog.create_post("selenium", "one of automation tools")
        app.blogs = dict({"automation": blog})

        with patch("application.print_post") as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])



    def test_print_post(self):




        #blog = Blog("Love", "Kingsman")
        #blog.create_post("Forever Love", "Siblings")
        #application.blogs = dict({"Love": blog})
        post = Post("Forever Love", "Siblings")
        expected = '''---Forever Love---Siblings'''

        with patch("builtins.print") as mocked_print:
            app.print_post(post)
            #mocked_print.assert_called_with(expected)
            self.assertEqual(app.POST_TEMPLATE, '''---{}---{}''' )


    def test_ask_create_post(self):
        blog = Blog("Love", "Kingsman")
        app.blogs = dict({"Love": blog})

        with patch("builtins.input") as mocked_input:

            mocked_input.side_effect=("Love", "Love Forever2", "Friendship")
            app.ask_create_post()

            #self.assertEqual(blog.posts[0].name, "Love Forever2")
            mocked_input.assert_called()










































