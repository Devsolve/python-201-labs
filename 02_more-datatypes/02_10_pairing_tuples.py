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
print(sorted_my_list)

my_tuple_list=[]
if len(sorted_my_list)%2!=0:
     sorted_my_list.append(0)
     
"""First way"""

temp_list=[] 
for num in sorted_my_list:
     if len(temp_list)==2:
          print(f'if:{num}')
          tuple_list=tuple(temp_list)
          print(f'tuple_list:{tuple_list}')
          my_tuple_list.append(tuple_list)
          temp_list.clear()
          temp_list.append(num)
     else:
          print(f'else:{num}')
          temp_list.append(num)
          if sorted_my_list[-1]==num:
               tuple_list=tuple(temp_list)
               print(f'tuple_list:{tuple_list}')
               my_tuple_list.append(tuple_list)

"""Second way"""

for i in range(0,len(sorted_my_list)-1,2):
     tuple_list=(sorted_my_list[i],sorted_my_list[i+1])
     my_tuple_list.append(tuple_list)


print(my_tuple_list)

