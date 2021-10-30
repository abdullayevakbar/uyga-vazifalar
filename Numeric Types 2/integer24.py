from math import sqrt ,pow ,pi , tan, cos
x,y=map(float,input().split())
ans=sqrt(x+pow(abs(y)+2,0.25))
print(round(ans,2))