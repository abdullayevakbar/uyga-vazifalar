from math import sqrt ,pow ,pi , tan, cos, sin ,e
a,x=map(float,input().split())
ans=sqrt(pow(e,x)+a/(x*x+2))
print(ans)