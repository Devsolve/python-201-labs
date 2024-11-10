# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def get_list():
     list_1 = [1, 2, 3, 4, 5, 6, 7]
     return list_1

def get_sum_of_list():
     list_1 = get_list()
     sum_list = sum(list_1)
     return sum_list

def get_length_list():
     list_1 = get_list()
     list_len = len(list_1)
     return list_len

def average_list():
     sum_list = get_sum_of_list()
     list_len = get_length_list()
     average = sum_list/list_len
     return average

average = average_list()
print(f'average: {average}')