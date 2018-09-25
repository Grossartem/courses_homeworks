import random
number = int(input("Please enter the number,number >0: "))
random_sample = random.sample(range(0,number + 1),number)
print(random_sample)

