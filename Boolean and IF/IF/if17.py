def if_find_num_digits_max(a,b):
    if(a%10+a//10>b%10+b//10):
        return a
    else:
        return b