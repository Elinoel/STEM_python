#my first python list
numbers = [45, 34, 67, 90]
#print (len(numbers))

#print(sum(numbers))
#for i in range(len(numbers)):
#    print(numbers[i])

#list methods
#1.index
# print(numbers.index(34))
# names = ["python", "c++", "java", "typescript"]
# print(names.index("c++"))

#append - adds an element to the end of a list

#before appending
# for i in range(len(numbers)):
#     print(numbers[i])

# print("\n")
# numbers.append(90)

# #after appending
# for i in range(len(numbers)):
#     print(numbers[i])

#SORT

#COUNT - returns the number of times an element occurs in a list.
# print(numbers.count(67))

#POP - removes an element at a given element and returns that element
# print(numbers.pop(2))

#INSERT - inserts an element "x" at an index y
# numbers.insert(2, 100)
# for i in range(len(numbers)):
#    print(numbers[i])

#REMOVE - removes the first occurence of an element
# numbers.remove(67)
 
#SORT- Sorts the elements
for i in range(len(numbers)):
   print(numbers[i])

print("\n")
#sort the list
numbers.sort()

# after sorting
for i in range(len(numbers)):
   print(numbers[i])