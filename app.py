'''
This class implements the app which is a client to both blog and post classes
'''
from blog import Blog
MENU_PROMPT = 'Enter "c" to create a Blog, "l" to list blogs, "r" to read blogs, "p" to create a post, "q" to quit'
POST_TEMPLATE = 'Post title{}-Post content{}'
blogs = dict()
# ==============================================================================================================================
def menu():
    selection = input(MENU_PROMPT)
    while(selection!='q'):
        if(selection == 'c'):
            create_blog()
            break
        else:
            if(selection == 'l'):
                print_blog()
                break
            else:
                if(selection == 'r'):
                    read_blog()
                    break
                else:
                    if(selection == 'p'):
                        create_post()
                        break
        break
# ==============================================================================================================================
'''
SELECTION = 'c'
'''
def create_blog():
    blog_title = input('Enter the blog title you want to create  : ')
    blog_author = input('Enter the blog author : ')
    blogs[blog_title] = Blog(blog_title,blog_author)
# ==============================================================================================================================
'''
SELECTION = 'l'
'''
def print_blog():
    for key, blog in blogs.items():
        print('{} '.format(blog.__repr__()))
# ==============================================================================================================================
'''
SELECTION = 'p'
'''
def create_post():
    blog_title = input('Enter the blog title you want to write a post in   : ')
    post_title = input('Enter the post title you want to create in a blog : ')
    post_content = input('Write your Post : ')
    blogs[blog_title].create_post(post_title,post_content)
# =============================================================================================================================
'''
SELECTION = 'r'
'''
def read_blog():
    title = input('Enter the blog title you want to read  : ')
    print_posts(blogs[title])
def print_posts(blog):
    for post in blog.posts:
        print_post(post)
def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))
# =============================================================================================================================