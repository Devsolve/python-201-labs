# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
my_list = randlist

"""First Way"""

sorted_my_list = sorted(my_list)
even_list= []
odd_list = []
for num in sorted_my_list:
     if num%2==0:
          even_list.append(num)
     else:
          odd_list.append(num)
          
my_tuple_list = [tuple(even_list),tuple(odd_list)]

# print(my_tuple_list)

"""Second Way"""
my_anothe_tuple_list = [
     tuple(num for num in sorted(my_list) if num%2==0) ,
     tuple(num for num in sorted(my_list) if num%2!=0)
]

print(my_anothe_tuple_list)