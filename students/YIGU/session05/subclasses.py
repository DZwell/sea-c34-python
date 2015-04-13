# 1. Is var from super class and subclass the same?


def q1():
    class Circle(object):
        color = "red"
        diameter = 3

    class NewCircle(Circle):
        color = "blue"

    c = Circle
    nc = NewCircle
    c.diameter = 4
    print c.diameter
    print nc.diameter
    print c.diameter is nc.diameter

# Answer: True

# 2. What happen if a inherited from b and b inherited from a?

def q2():
    class Circle2(NewCircle2):
        color = "red"
        diameter = 3


    class NewCircle2(Circle2):
        color = "blue"

# Answer: Error out because Cirle2 don't know what is NewCircle2.

# 3. What about b and c inherited from a and d inherited from b and c?


def q3():
    class a():
        def p(self):
            print ("p of A called")

    class b(a):
        def p(self):
            print ("p of B called")

    class c(a):
        def p(self):
            print ("p of C called")

    class d(b, c):
        pass

    q = d()
    q.p()

# Answer: p of B called

# 4. From q3, what will happen if I use issubclass() on d to a, b and c?

def q4():
    class a():
        def p(self):
            print ("p of A called")

    class b(a):
        def p(self):
            print ("p of B called")

    class c(a):
        def p(self):
            print ("p of C called")

    class d(b, c):
        pass

    print issubclass(d, a)
    print issubclass(d, b)
    print issubclass(d, c)

# Answer is true, true and true
