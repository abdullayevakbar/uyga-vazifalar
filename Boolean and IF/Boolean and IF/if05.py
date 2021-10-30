def if_check_middle_number(a,b,c):
    x=a
    y=a
    if(b>x):
        x=b
    if(c>x):
        x=c
    if(b<y):
        y=b
    if(c<y):
        y=c
    return a+b+c-x-y