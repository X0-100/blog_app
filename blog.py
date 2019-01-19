'''
This file implements the blog functionality
for a user to write a blog containing a blog title, a blog author and a reference to post
'''

from post import Post

class Blog:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def create_post(self, title, content):
        self.posts.append(Post(title,content))

    def json(self):
        return({
            'title' : self.title,
            'author' : self.author,
            'posts' : [post.json() for post in self.posts]
        })

    def __repr__(self):
        return('Title of the blog is {} & Author of the blog is {} for {} post{}'
              .format(self.title, self.author, len(self.posts), 's' if (len(self.posts) != 1) else '' ))