# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
user_list = list(map(str,input().split()))

user_list = [tuple(x) for x in user_list]

print(user_list)
     