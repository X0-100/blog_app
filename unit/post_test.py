'''
This file implements test cases written for post
Below are the unit test methods -

'''
from unittest import TestCase
from post import Post

class TestPost(TestCase):

    def test_post_created(self):
        post1 = Post('HelloWorld!','This is HelloWorld!')
        self.assertEqual('HelloWorld!', post1.title)
        self.assertEqual('This is HelloWorld!', post1.content)
        post2 = Post('HelloWorld1!','This is HelloWorld1!')
        self.assertEqual('HelloWorld1!', post2.title)
        self.assertEqual('This is HelloWorld1!', post2.content)

    def test_json(self):
        post3 = Post('HelloWorld3!', 'This is HelloWorld3!')
        self.assertDictEqual({'title': 'HelloWorld3!', 'content': 'This is HelloWorld3!'}, post3.json())





