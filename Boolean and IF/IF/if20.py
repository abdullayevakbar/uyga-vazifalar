def if_two_digits_pisitive_even(age):
    return (age>0 and age>9 and age<100 and (age%10+age//10)%2==0)