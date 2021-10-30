from math import sqrt ,pow ,pi , tan, cos
x,y=map(float,input().split())
ans=1/3+cos(y+x*x)**2
print(round(ans,2))