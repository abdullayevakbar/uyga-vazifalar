from math import sqrt ,pow ,pi , tan, cos, sin ,e
x=float(input())
ans=sqrt(2*tan(x+2)-cos(x+pow(2,x)))
print(round(ans,2))