'''
Allows user to create post with post title and post content
'''

class Post:
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def json(self):
        #return({self.title : self.content})
        return(
            {'title' : self.title,
            'content' : self.content}
        )
