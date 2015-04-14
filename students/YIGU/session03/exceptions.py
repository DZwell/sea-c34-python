def q1():
    """What if I put finally in a loop with a break?"""
    while True:
        try:
            x = int(raw_input("Please enter a number: "))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
        finally:
            print "Executing finally"

    # Answer: finally still ran
    # Please enter a number: 10
    # Executing finally
q1()


def q2():
    """Can I use except more than once? For example,
     try XX, expect XX,expect XX"""
    try:
        f = open('test.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as e:
        print "I/O error %s: %s" % (e.errno, e.strerror)
    except ValueError:
        print "Could not convert data to an integer."
    except:
        print "Unexpected error"
        raise

# Answer: Yes

q2()
