def if_exchange_number(n):
    a=(n%10)*10+n//10
    if(a<=n):
        return True
    return False