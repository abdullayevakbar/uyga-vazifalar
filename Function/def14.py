from  math import  pi
def func(x):
    s=1
    s*=x%10
    x//=10
    s *= x % 10
    x //= 10
    s *= x % 10
    x //= 10
    s *= x % 10
    x //= 10
    s *= x % 10
    return s
a=int(input())
print(func(a))