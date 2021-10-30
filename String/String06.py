def find_count_digits(a):
    s=0
    if(a[0]>='0' and a[0]<='9'):
        s+=1
    if (a[1] >= '0' and a[1] <= '9'):
        s += 1
    if (a[2] >= '0' and a[2] <= '9'):
        s += 1
    if (a[3] >= '0' and a[3] <= '9'):
        s += 1
    if (a[4] >= '0' and a[4] <= '9'):
        s += 1
    return s