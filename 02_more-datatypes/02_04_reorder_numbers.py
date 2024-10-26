# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

# take input from user 10 numbers
user_list = list(map(int, input().split()))
# sort them in assending order


'''----First way----'''
sorted_list = sorted(user_list)
print(sorted_list)
# iterate the list 
sorted_user_list_even = [x for x in sorted_list if x%2==0]
sorted_user_list_odd = [x for x in sorted_list if x%2!=0]
# check and print first divisible by 2 and not divisible by 2
sorted_user_list = sorted_user_list_even + sorted_user_list_odd
print(*sorted_user_list, sep=", ")


'''----Second way----'''
sorted_user_list = sorted(user_list)
sorted_user_list = [x for x in sorted_user_list if x % 2 == 0] + [x for x in sorted_user_list if x % 2 != 0]

# Print the sorted list
print(*sorted_user_list, sep=", ")