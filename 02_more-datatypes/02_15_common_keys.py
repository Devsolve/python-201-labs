# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = dict(dict_1) # copy dict_1

for d in dict_2: # iterate the dict_2
     if d in result: # find the dict_2 key is present or not, if yes then update the value
          result[d] += dict_2[d]
     else:
          result[d] = dict_2[d]

print(result)