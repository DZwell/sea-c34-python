def methods():
    """
    Can you call a static method from a class method?
    """
    class Classy(object):
        @classmethod
        def a_class_method(cls, x, y):
            print "inside class ", cls

            class StaticSubtractor(object):
                @staticmethod
                def subtract(a, b):
                    return a - b
            print StaticSubtractor.subtract(x, y)
    print Classy.a_class_method(5, 3)

methods()
# yes
