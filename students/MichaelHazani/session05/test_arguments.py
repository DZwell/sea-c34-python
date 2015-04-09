import arguments

localx = arguments.x


def test_tupleexperiment():
    """test method tupleexperiment in the arguemnts.py module"""

    assert(arguments.tupleexperiment(localx) == (4, 3, 4, 5, 6))
