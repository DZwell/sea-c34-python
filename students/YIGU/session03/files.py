def q1():
    """What happen when I try to read (500) with an empty file."""
    header_size = 5000
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

    # Answer: nothing. No error.

q1()


def q2():
    """Can I read hidden file?"""
    import io
    f = io.open('.secrets.txt', encoding='utf-8')
    secret_data = f.read()
    print secret_data
    f.close()

    # Answer:Yes

q2()
