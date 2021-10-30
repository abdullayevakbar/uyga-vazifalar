from math import sqrt ,pow ,pi , tan, cos, sin ,e
n=int(input())
ans=((n//1000+5)*1000+((n//100)%10+5)*100+((n//10)%10+5)*10+(n%10+5))
print(ans)