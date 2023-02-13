#getting random numbers
from random import randint

nums= []


for i in range (20):
    number = randint(0,100)
    nums.append(number)

print(nums)