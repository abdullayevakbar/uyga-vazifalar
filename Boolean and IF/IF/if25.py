def if_middle_ages_little_user(user_1,user_2,user_3):
    s = 2021 - user_1
    s += 2021 - user_2
    s += 2021 - user_3
    ans=0
    if(2021 - user_1<s/3):
        ans+=1
    if (2021 - user_2 < s / 3):
        ans += 1
    if (2021 - user_3 < s / 3):
        ans += 1

    return ans