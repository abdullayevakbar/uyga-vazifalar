def if_check_find_number_digit(n):
    if(n//10)==0:
        return 1
    n//=10
    if (n // 10) == 0:
        return 2
    n //= 10
    if (n // 10) == 0:
        return 3
    n //= 10
    if (n // 10) == 0:
        return 4
    n //= 10
    if (n // 10) == 0:
        return 5
    n //= 10
    if (n // 10) == 0:
        return 6