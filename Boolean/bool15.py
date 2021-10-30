def sum_digits_check_odd_1(n):
    s=0
    s+=n%10
    n//=10
    s += n % 10
    n //= 10
    s += n % 10
    n //= 10
    s += n % 10
    n //= 10
    s += n % 10
    return (s//10)>0