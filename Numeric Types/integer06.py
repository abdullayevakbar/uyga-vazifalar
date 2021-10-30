from math import sqrt ,pow
r,n,a,b=map(int,input().split())
ans=pow(1-r/100,n)/(sqrt(a*a+b*b))
print(ans)