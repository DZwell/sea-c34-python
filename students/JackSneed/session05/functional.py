def lamday():
    """Can I use lambda/lambda?"""
    sea = lambda x, y: x+y
    hawks = lambda x, y: x-y
    birds = ((hawks(20, 4))/(sea(2, 6)))
    print birds

lamday()


def filtering():
    """Can I filter out a large list of numbers divisible by 4?"""
    l = range(51)
    quarter = filter(lambda x: not x % 4, l)
    print quarter

filtering()


def reduction():
    """Can I reduce and get the product od two list?"""
    m = [6, 7, 8, 9, 10]
    n = [11, 12, 13, 14, 15]
    o = reduce(lambda x, y: x*y, m)
    p = reduce(lambda x, y: x*y, n)
    print o*p

reduction()
