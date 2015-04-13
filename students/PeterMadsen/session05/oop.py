# Question One and Test
def mulltiply_functions(object1, object2):
    """
    Can you write a function that multiples different values
    Without knowing in advance what the return values of the functions
    are? Function will raise an error if you cannot multiply the types.

    """
    try:
        one = object1
        two = object2
        return one * two
    except TypeError as e:
        print(e)


def test_function_1(value):
    return value


def test_function_2(value):
    return value

print(mulltiply_functions(test_function_1(4), test_function_2(5)))
print(mulltiply_functions(test_function_1(4), test_function_2("hi ")))
print(mulltiply_functions(test_function_1(4), test_function_2(lambda x: x)))


# Question two
def question_two():
    """
    In this question I'm trying to explore the difference between "is - a"
    and "has - a" Relationships. I'm trying to understand inheritance.

    The PuzzlePiece and the BorderPiece classes are in an "is - a"
    relationship, and those classes are in a "has - a" relationship with the
    Puzzle class.

    """
    class PuzzlePiece:

        def __init__(self, tabs, blanks, sides):
            self.tabs = tabs
            self.blanks = blanks
            self.sides = sides

    # Border piece 'is - a' type of Puzzle Piece
    class BorderPiece(PuzzlePiece):

        def __init__(self, tabs, blanks):
            PuzzlePiece.__init__(self, tabs, blanks, 3)

    # Puzzle class 'has' puzzle pieces
    class Puzzle:

        def __init__(self, pieces, box):
            self.pieces = pieces
            self.box = box
