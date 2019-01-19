'''
This file tests blog
Below are the unit test cases -
-> test_create_blog
-> test_repr_
-> test_multiple_repr_
'''

from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):
        blog1 = Blog('HelloWorld1','@goku')
        self.assertEqual('HelloWorld1', blog1.title)
        self.assertEqual('@goku', blog1.author)
        self.assertListEqual([], blog1.posts)

    def test_repr_(self):
        blog2 = Blog('HelloWorld2','@quagmire')
        blog3 = Blog('HelloWorld3','@louis')
        self.assertEqual('Title of the blog is HelloWorld2 & Author of the blog is @quagmire for 0 posts', blog2.__repr__())
        self.assertEqual('Title of the blog is HelloWorld3 & Author of the blog is @louis for 0 posts', blog3.__repr__())

    def test_multiple_repr_(self):
        blog4 = Blog('HelloWorld4','@peter')
        blog4.posts = ['object blog - HelloWorld4']
        self.assertEqual('Title of the blog is HelloWorld4 & Author of the blog is @peter for 1 post', blog4.__repr__())
        blog5 = Blog('HelloWorld5','@chris')
        blog5.posts = ['object blog - HelloWorld5']
        self.assertEqual('Title of the blog is HelloWorld5 & Author of the blog is @chris for 1 post', blog5.__repr__())
        blog5.posts.append(['object blog - HelloWorld5 - post appended'])
        self.assertEqual('Title of the blog is HelloWorld5 & Author of the blog is @chris for 2 posts', blog5.__repr__())


