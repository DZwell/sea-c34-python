def args_test(x, *args):
    """Does *args catch explicitly set positional arguments as well?"""
    print(args)


args_test(1, 2, 3, 4)
# result: No. *args only catches extra, non-set arguments.


def kwargs_test(this=5, **kwargs):
    """Does *kwargs catch explicitly set keyword arguments as well?"""
    print(kwargs)


kwargs_test(this=5, that=10)
# result: No. Same behavior as *args.


def empty_args_kwargs(*args, **kwargs):
    """Do args and kwargs exist in function if no arguments passed?"""
    print(args)
    print(kwargs)


empty_args_kwargs()
# result: Yes, they exist as an empty tuple and dict, respectively.

