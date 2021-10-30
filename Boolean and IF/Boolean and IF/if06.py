def if_check_dekart_kordinata(x,y):
    if(x>0 and y>0):
        return "I - chorak"
    if(x<0 and y>0):
        return "II - chorak"
    if(x<0 and y<0):
        return "III - chorak"
    if(x>0 and y<0):
        return "IV - chorak"