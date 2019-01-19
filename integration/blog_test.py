'''
This is a system test
Where the tests covers blog which will act as a system to create a blog first and then a post written inside it
'''

from blog import Blog
from unittest import TestCase

class TestBlog(TestCase):

    def test_create_post(self):

        blog1 = Blog('Blog title1','Blog Author1')
        blog1.create_post('PostTitle', 'Content : This is Hello World from the Blog Author1')
        self.assertEqual('PostTitle', blog1.posts[0].title)
        self.assertEqual('Content : This is Hello World from the Blog Author1',blog1.posts[0].content)

        blog2 = Blog('BlogTitle2', 'Blog Author2')
        blog2.create_post('PostTitle2', 'Content : This is Hello World from Blog Author2')
        self.assertEqual('PostTitle2', blog2.posts[0].title)
        self.assertEqual('Content : This is Hello World from Blog Author2', blog2.posts[0].content)
        blog2.create_post('A Random Post', 'A random Content')
        self.assertEqual('A Random Post', blog2.posts[1].title)
        self.assertEqual('A random Content', blog2.posts[1].content)

    def test_json_no_posts(self):
        blog3 = Blog('ABC', 'DEF')
        expected = {'title' : 'ABC', 'author' : 'DEF', 'posts' : []}
        self.assertDictEqual(expected, blog3.json())

    def test_json_with_posts(self):
        blog4 = Blog('EFG', 'LKJ')
        blog4.create_post('ChampagneSupernova','HowManySpecialPeopleChange')
        expected = {'title' : 'EFG', 'author' : 'LKJ', 'posts' : [{'title' : 'ChampagneSupernova', 'content' : 'HowManySpecialPeopleChange'}]}
        self.assertDictEqual(expected, blog4.json())
