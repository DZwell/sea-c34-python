class SpecialList(list):
    """Can you overwrite the magic methods of builtins?"""
    def __init__(self):
        list.__init__(self)

    def __str__(self):
        for item in self:
            return str(self * 2)

if __name__ == '__main__':
    sl = SpecialList()
    sl.append(1)
    sl.append(3)
    sl.append(6)
    print(sl)
