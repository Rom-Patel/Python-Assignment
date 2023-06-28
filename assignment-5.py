#Take input from the user of 5 numbers and store it in a list.
lst = []
for i in range(5):
    num=int(input(f"Enter  number.{i + 1}: "))
    lst.append(num)


#Calculate the sum of all the elements in the list
print("Sum of all elements in the list :",sum(lst))


#Find the smallest number
print("Minimum number in the list:",min(lst))


#Find the largest number
print("Maximum number in the list:",max(lst))


#Display list in ascending order
lst.sort()
print("Sorting list in Ascending order: ",lst)


#Display list in descending order
lst.sort(reverse=True)
print("Sorting list in Descending order: ",lst)


#Convert list into tuple
t1=tuple(lst)
print("List: ",lst)
print("Tupple: ",t1)


# Delete the list
del lst
# print(lst)
