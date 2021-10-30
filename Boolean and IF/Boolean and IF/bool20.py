def check_five_digit_number_1(a):
    x = a % 10
    a //= 10
    if x <= a % 10:
        return False
    x = a % 10
    a //= 10
    if x <= a % 10:
        return False
    x = a % 10
    a //= 10
    if x <= a % 10:
        return False
    x = a % 10
    a //= 10
    if x <= a % 10:
        return False
    return True