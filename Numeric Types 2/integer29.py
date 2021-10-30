from math import sqrt ,pow ,pi , tan, cos, sin ,e
n=int(input())
ans=((n//1000)**2*1000+((n//100)%10)**2*100+((n//10)%10)**2*10+(n%10)**2)
print(ans)