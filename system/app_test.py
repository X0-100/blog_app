'''
This file will implement writing tests for app interface
'''

from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from post import Post
import app


class AppTest(TestCase):


    def setUp(self):
        blog = Blog('Blog Title : DEFAULT', 'Blog Author : DEFAULT')
        app.blogs = {'Blog Title : DEFAULT': blog}


    '''
    -----    The below tests are written by patching/mocking the function menu in app ----------
    '''

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.p_create_post') as mocked_create_post:
                mocked_input.side_effect = ('p', 'Blog Title : Sunflower', 'Post Title : Sunflower by Post Malone',
                                            'Post Content : Unless I struck by you, You are the sunflower')
                app.menu()
                mocked_create_post.assert_called()

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.c_create_blog') as mocked_create_blog:
                mocked_input.side_effect = ('c', 'Blog Title : Sunflower', 'Blog Author : Post Malone')
                app.menu()
                mocked_create_blog.assert_called()

    def test_menu_print_blog_I(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.l_print_blog') as mocked_print_blog:
                mocked_input.side_effect = ('l')
                app.menu()
                mocked_print_blog.assert_called()

    def test_menu_print_blog_II(self):
        with patch('builtins.input',return_value='l') as mocked_input:
            with patch('app.l_print_blog') as mocked_print_blog:
                app.menu()
                mocked_print_blog.assert_called()

    def test_menu_read_blog(self):
        with patch('builtins.input', return_value='r') as mocked_input:
            with patch('app.r_read_blog') as mocked_read_blog:
                app.menu()
                mocked_read_blog.assert_called()

    '''
    Below tests are written for validating blog and post data that are getting created in app.
    Patches have been written by directly calling the blog and post functions that otherwise
    were validated by calling app.menu() from above
    '''

    def test_validate_create_blog_data(self):
        with patch('builtins.input') as mocked_input:
            #mocked_input.side_effect = ('Blog : 30STM','Blog Author : Jared Leto')
            app.c_create_blog()
            self.assertIsNotNone(app.blogs.get('Blog Title : DEFAULT'))
            self.assertIsNone(app.blogs.get(''))

    def test_validate_read_blog_data(self):
        with patch('builtins.input', return_value='Blog Title : DEFAULT'):
            with patch('app.print_posts') as mocked_print_posts:
                app.r_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Blog Title : DEFAULT'])

    def test_validate_post_data_I(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Blog Title : DEFAULT','Post Title : DEFAULT','Post Content : DEFAULT')
            app.p_create_post()
            self.assertEqual(app.blogs['Blog Title : DEFAULT'].posts[0].title, 'Post Title : DEFAULT')
            self.assertEqual(app.blogs['Blog Title : DEFAULT'].posts[0].content, 'Post Content : DEFAULT')

    def test_validate_post_data_II(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Blog Title : DEFAULT', 'post title 1', 'post content 2')
            app.p_create_post()
            self.assertEqual(app.blogs['Blog Title : DEFAULT'].posts[0].title, 'post title 1')
            self.assertEqual(app.blogs['Blog Title : DEFAULT'].posts[0].content,'post content 2')
            mocked_input.side_effect = ('Blog Title : DEFAULT', 'post title 2', 'post content 2')
            app.p_create_post()
            self.assertEqual(app.blogs['Blog Title : DEFAULT'].posts[1].title,'post title 2')
            self.assertEqual(app.blogs['Blog Title : DEFAULT'].posts[1].content,'post content 2')

    def test_validate_print_blog_data(self):
        blog1 = Blog('AnotherBlog','AnotherAuthor')
        app.blogs = {'AnotherBlog' : blog1}
        with patch('builtins.print') as mocked_print:
            app.l_print_blog()
            #The below line is the expected call which should match the Actual Call
            mocked_print.assert_called_with('-Title of the blog is AnotherBlog & Author of the blog is AnotherAuthor for 0 posts')











