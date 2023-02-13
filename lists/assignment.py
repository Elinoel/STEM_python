#number 1
nums = []
list_length = 4

for i in range(list_length):
    number = eval(input("Enter a number"))
    nums.append(number)

for num in nums:
    print(num)

print("\n")

print(nums[-1])

nums.sort()
print(nums)

print(nums[-2])