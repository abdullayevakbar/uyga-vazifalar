def if_find_idx_1(a,b,c,d):
    if (a != b and a != c):
        return 1
    if (b != a and b != c):
        return 2
    if(c!=b and c!=d):
        return 3
    return 4