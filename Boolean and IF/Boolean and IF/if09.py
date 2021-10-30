def if_check_number_odd_even(a):
    if(a==0):
        return "son 0 ga teng"
    x=abs(a)%2
    if(a>0):
        if(x):
            return "musbat toq son"
        else:
            return "musbat juft son"
    else:
        if(x):
            return "manfiy toq son"
        else:
            return "manfiy juft son"
