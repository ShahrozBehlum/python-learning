inputVal1 = input('Enter first value: ')
inputVal2 = input('Enter second value: ')

def convert(val):
    try:
        return int(val)
    except ValueError:
        return val

def multiply(val1, val2):
    val1 = convert(val1)
    val2 = convert(val2)

    # If both are numbers → multiply normally
    if isinstance(val1, int) and isinstance(val2, int):
        return val1 * val2

    # If one is string and other is int → repeat string
    if isinstance(val1, str) and isinstance(val2, int):
        return val1 * val2

    if isinstance(val2, str) and isinstance(val1, int):
        return val2 * val1

    # If both strings → combine them
    return val1 + val2

result = multiply(inputVal1, inputVal2)
print(result)