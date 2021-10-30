def two_digit_number_check_1(n):
	return (n%10+(n//10)%10+n//100)//10>0