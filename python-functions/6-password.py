def validate_password(password):
    if len(password) < 8:
        return False
    upper = False
    lower = False
    digit = False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
    if ' ' in password:
        return False
    return upper and lower and digit