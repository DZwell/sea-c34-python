def multiple_errors():
    """Check to see of I can except multiple errors"""

    try:
        obvious_error()
    except (TypeError, NameError) as bad_stuff:
        print type(bad_stuff)
        print(bad_stuff)

multiple_errors()
# This example only prints one exception

def finally_corrected():
    """Check to see of I can clean up error with 'finally'."""

    try:

        six = '3' + 3
    except (TypeError) as clean_stuff:
        print type(clean_stuff)
        print(clean_stuff)
    finally:
        six = 3 + 3
        print(six)

finally_corrected()
