from  math import  pi
def func(x):
    s=0
    s+=x%2
    x//=10
    s += x % 2
    x //= 10
    s += x % 2
    x //= 10
    s += x % 2
    x //= 10
    s += x % 2
    return s
a=int(input())
print(func(a))