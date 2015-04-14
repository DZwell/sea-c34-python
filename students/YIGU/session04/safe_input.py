# taks10 safe_input.py


def safe_input(note):
    """This function catch excepition from raw_input function and return None"""
    try:
        i = raw_input(note)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return i
