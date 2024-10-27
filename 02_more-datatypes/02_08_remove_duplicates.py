# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# first ways
frst_unique_list = list(set(list_))
print(frst_unique_list)


# second way
unique_list = []
for num in list_:
     if num in unique_list:
          continue
     else:
          unique_list.append(num)
          
print(unique_list)
     
