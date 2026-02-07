import numbers


def validate_number(value):
    """
    Validate that value is a numeric type but not a boolean.

    Args:
        value: The value to validate.

    Raises:
        TypeError: If value is not a number or is a boolean.
    """
    if not isinstance(value, numbers.Number):
        raise TypeError("must be a number")

    if isinstance(value, bool):
        raise TypeError("can't be bool")
