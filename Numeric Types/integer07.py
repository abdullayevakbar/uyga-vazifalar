from math import sqrt
x,y,x1,y1=map(float,input().split())
ans=sqrt((x-x1)**2+(y-y1)**2)
print(round(ans))