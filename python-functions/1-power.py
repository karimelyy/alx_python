def pow(a, b):
    if b >= 0:
        return a ** b
    else:
        return 1 / (a ** abs(b))