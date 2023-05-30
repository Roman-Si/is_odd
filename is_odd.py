def is_odd(x):
    """
    Function determine if number is odd.
    Return True if input is odd integer.
    Return False if input is even integer.
    Return Type Error if input is not integer.
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    return x % 2 != 0


assert is_odd.__doc__ is not None

has_raised = False
try:
    is_odd("This is a string")
except TypeError as e:
    has_raised = True

assert has_raised

assert is_odd(3)