from blog import Blog

blogs = dict()
MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blog, 'r' to read one, 'p' to create a post, 'q' to quit"
POST_TEMPLATE = '''---{}---{}'''
def menu():

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

    print_blogs()




def create_blog():

    title = input("Whats the title of the post? ")
    author = input("Who is the writer? ")
    blogs[title] = Blog(title, author) #set the blogs as dict, then get value from blogs[key]
    print(blogs[title])


def print_blogs():
    for key, blog in blogs.items():
        print("- {}".format(blog))
        #print(key)
        #print(blog)



def read_blog():
    blog_title = input("Enter the blog title you want to read:")

    for i in blogs[blog_title].posts:
        try:
            len(blogs[blog_title].posts) != 0
            print(i)

        except KeyError:
            print("There is no such title")




"""    
    print_posts(blogs[blog_title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):

    print(POST_TEMPLATE.format(post.name, post.content))
"""

def ask_create_post():
    blog_name = input("Enter the blog title you want to write post in: ")
    name = input("Whats the name of the post: ")
    content = input("enter ur post content: ")

    blogs[blog_name].create_post(name, content)


menu()






