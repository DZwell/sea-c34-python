def function_list(n):
    flist = []
    for i in range(n +1):
        flist.append(lambda x, y = i: x+y)

    return flist

if __name__ == '__main__':

    newlist = function_list(4)
    print newlist[2](5)
    print newlist[0](2)
    print newlist[1](2)
