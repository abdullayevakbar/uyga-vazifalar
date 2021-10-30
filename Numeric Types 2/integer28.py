from math import sqrt ,pow ,pi , tan, cos, sin ,e
n=int(input())
ans=(n%10)**2
n//=10
ans+=(n%10)**2
n//=10
ans+=(n%10)**2
n//=10
ans+=(n%10)**2
n//=10
ans+=(n%10)**2
print(ans)