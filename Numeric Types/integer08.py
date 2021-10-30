from math import sqrt
x,y,x1,y1,x2,y2=map(float,input().split())
a=sqrt((x-x1)**2+(y-y1)**2)
b=sqrt((x2-x1)**2+(y2-y1)**2)
c=sqrt((x-x2)**2+(y-y2)**2)
p=(a+b+c)/2
ans=sqrt(p*(p-a)*(p-b)*(p-c))
print(round(p*2,2),round(ans,2))