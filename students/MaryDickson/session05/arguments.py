# 3 questions

# Q1: build a dictionary then stick it in a string, will this work with ints?:

d = {u"last": u"Dickson", u"first": u"Mary", "amount": 100}
print u"Thank you, {first} {last}, for your donation of {amount}.".format(**d)


# Q2: what's an arg and kwarg?

def f(*args, **kwargs):
    print(u"the positional arguments are: %s" % unicode(args))
    print type(args)
    print(u"the optional arguments are: %s" % unicode(kwargs))
    print type(kwargs)

print f(2, 3, this=5, that=7)
print f("hello", you="victor", me="mary")
print f(0, 2, 6, 8)

# Q3: ok, so if kwargs are actually a dictionary, can I then loop through it
# and return something else?


def f2(*args, **kwargs):
    print(u"the positional arguments are: %s" % unicode(args))
    print type(args)
    print(u"the optional arguments are: %s" % unicode(kwargs))
    print type(kwargs)
    for k, v in kwargs.items():
        kwargs[k] = str(v) + str(args)
    return kwargs

print f2(2, 3, this=5, that=7)
print f2("hello", you="victor", me="mary")
print f2(0, 2, 6, 8)

# yes, but it doesn't make a ton of sense.
