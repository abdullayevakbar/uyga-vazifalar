def if_find_sum_number_digits(n):
    s = 0
    s += n % 10
    n // 10
    s += n % 10
    n // 10
    s += n % 10
    n // 10
    s += n % 10
    n // 10
    s += n % 10
    n // 10
    s += n % 10
    n // 10
    s += n % 10
    n // 10
    return s

