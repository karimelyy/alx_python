def convert_to_celsuis(fahrenheit):
    if fahrenheit == -459.67:
        celsius = -273.15
    else:
        celsius = (fahrenheit - 32) * (5 / 9)
    return celsius
