def if_car_score_draver_age(driver_age,score):
    s=0.0
    if(driver_age<18):
        s+=576000.0
    if(score>60):
        s+=287000
    return s


