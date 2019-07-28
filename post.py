class Post:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):

        return "{} and {}".format(self.name, self.content)




    def json(self):
        return {
            "title":self.name,
            "content":self.content,
        }