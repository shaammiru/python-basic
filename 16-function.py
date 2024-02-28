def say_hello(name):
    """Print a greeting message to the user

    Args:
        name (string): name of the user
    """

    print(f"Hello {name}")


def multiply(num1, num2=1):
    """Multiply two numbers

    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int: the result of the multiplication
    """

    return num1 * num2


say_hello("John")

result = multiply(4, 5)
print(result)

# Anonymus function
# add = lambda x, y: x + y


def minimal(a, b):
    if a == b or a < b:
        return a
    else:
        return b


print(minimal(3, 2))
