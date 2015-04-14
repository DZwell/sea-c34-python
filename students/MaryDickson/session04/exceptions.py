# questions about the exceptions section in slides 4

list = [0, 1, 4, 8, 100, 1001]

def printitem(list, num):
    """
    Can I throw a warning message if number not in range?
    """
    try:
        return list[num]
    except:
        return(u"oops not long enough")
    finally:
        list.append(34)

print list
print printitem(list, 2)
print printitem(list, 10)
print list


def add_donation(dict, name, amount)
    if name in dict.keys:
        try:
            name.value = int(raw_input(ask for donation amount))
        exception:
            name.value = int(raw_input(ask for donation amount))
        finally:
            add (name,value) to donorlist
