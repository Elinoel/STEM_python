#multiplying a list
# zeros = [0]*10
# print(zeros)

#adding two lists
# list_1=[89, 90]
# list_2=[34, 78]
# final_list = list_1+list_2
# print(final_list)

#slicing a list
# nums = [12, 13, 14, 15]
# print(nums[2:]) #this prints from index 2 henceforth

# get the maximum value in a list
# nums = [89, 4]
# print(max(nums))

# getting the minium value in a list
# nums = [89, 4]
# print(min(nums))

#CREATING LISTS
# nums = [] #empty list
# for i in range(10):
#     #inserts an element into the list
#     nums.append(i)

# for i in range(len(nums)):
#     print(nums[i])

#PRINTING A LIST OF EVEN NUMBERS
even_nums = []
for num in range (20):
    if(num % 2 == 0):
        even_nums.append(num)
for i in range(len(even_nums)):
    print(even_nums[i])
