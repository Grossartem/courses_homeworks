import random
number = random.randint (1000,1000000)
whole_division_thousands = number //1000
fourth_dig = (whole_division_thousands+10) % 10
print (number,fourth_dig)
