def if_check_temperature(Temp):
    a=Temp
    if(a<0):
        return "Freezing"
    if(a>0 and a<11):
        return "Very Cold"
    if(a>10 and a<21):
        return "Cold"
    if(a>20 and a<31):
        return "Normal"
    if(a>30 and a<41):
        return "Hot"
    if(a>40):
        return "Very Hot"