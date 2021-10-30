def if_check_triangle_make(a,b,c):
    b=0
    b+=(a+b>c)
    b+=(a+c>b)
    b+=(b+c>a)
    if(b==3):
        return "Yes"
    else:
        return "No"
