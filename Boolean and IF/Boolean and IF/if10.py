def if_check_digit_number_odd_even(a):
    x=a%2
    if(a//100)>0 and (a//1000)==0:
        if(x):
            return "Uch xonali toq son"
        else:
            return "Uch xonali juft son"
    if(a//10)>0 and (a//100)==0:
        if(x):
            return "Ikki xonali toq son"
        else:
            return "Ikki xonali juft son"