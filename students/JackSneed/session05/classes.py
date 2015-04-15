class Build(object):
    """Can I build a message with an instance os a class?"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Build("I think", " I got it!")

if __name__ == '__main__':
    print(p.x + p.y)
