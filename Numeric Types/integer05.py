import math
a,b=map(float,input().split())
ans=9*a*a*b-27*(a*b)**2+15*b*b
print(round(ans,2))