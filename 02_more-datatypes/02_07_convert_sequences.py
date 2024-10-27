# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

my_tuple_list = list(tuple(string))
my_tuple_list[0] = 'k'
my_tuple = tuple(my_tuple_list)
print(my_tuple)

my_str = ''.join([x for x in my_tuple_list])

# another way of doing
# my_str = ''
# for x in my_tuple_list:
#      my_str += x

print(my_str)