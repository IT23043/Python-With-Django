# https://github.com/IT23043/Python-With-Django/blob/main/Assignment-2/IMG_20250517_105416.jpg
def add(a, b):
    return a + b

def sub(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return -1
