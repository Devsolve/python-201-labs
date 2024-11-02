# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}


# take user input in string
input_str = input("Enter a string: ")
# create a empty dictionary
result = {}
# iterate the string
for c in input_str:
     if c in result: # if any string repeat multiple time then add them
          result[c] += 1
     else:
          result[c] = 1

print(result)