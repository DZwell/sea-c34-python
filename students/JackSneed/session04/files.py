def read():
    """Can I open and read a text file???"""

    import io

    f = io.open("hello_there.txt", "r")
    data = f.read()
    print(data)
    # Output: hello there
    f.close()

read()

def write():
    """Can I create text file?"""

    import io

    write_file = io.open('write_file.txt', 'w')
    for i in range(14):
        write_file.write("Add line: %i\n" % i)
        print(write_file)

write()
