'''
This file implements the app interface that will act
as a client for blog and post
'''
from blog import Blog
MENU_PROMPT = 'Enter "p" to create a post, "c" to create a blog, "l" to print a blog, "r" to read a blog, "q" to quit'
POST_TEMPLATE = 'Title of the post : {} content of the post : {}'
blogs = dict()

def menu():
    selection = input(MENU_PROMPT)
    while(selection != 'q'):
        if(selection == 'p'):
            p_create_post()
            break
        else:
            if(selection == 'c'):
                c_create_blog()
                break
            else:
                if(selection == 'l'):
                    l_print_blog()
                    break
                else:
                    if(selection == 'r'):
                        r_read_blog()
                        break

        break


def p_create_post():
    blog_title = input('Enter the Blog name you want to write a post for : ')
    post_title = input('Enter the Post title : ')
    post_content = input('Enter the Post Content : ')
    blogs[blog_title].create_post(post_title,post_content)

def c_create_blog():
    title = input('Enter  Blog Title  : ')
    author = input('Enter Blog Author : ')
    blogs[title] = Blog(title,author)

def l_print_blog():
    for key, blog in blogs.items():
        print('-{}'.format(blog.__repr__()))

def r_read_blog():
    blog_title = input('Enter the blog title you want to read : ')
    print_posts(blogs[blog_title])
def print_posts(blog):
    for post in blog.posts:
        print_post(post)
def print_post(post):
    return(POST_TEMPLATE.format(post.title, post.content))



