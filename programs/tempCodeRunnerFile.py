for num in args:
        result += num
    for key, value in kwargs.items():
        result += value
    return result