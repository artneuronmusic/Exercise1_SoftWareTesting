from post import Post

class Blog:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []


    def __repr__(self):
        return "{} by {} ({} post{} )".format(self.title, self.author, len(self.posts),
                                             's' if len(self.posts) != 1 else '')

    def create_post(self, name, content):
        self.posts.append(Post(name, content))


    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [i.json() for i in self.posts]
            #'posts': [post.josn() for post in self.posts]
        }

