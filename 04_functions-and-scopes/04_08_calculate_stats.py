# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_1):
  # define the function here
  max_num = max(list_1)
  print(f'max: {max_num}')
  
  min_num = min(list_1)
  print(f'min: {min_num}')
  
  sum_num = sum(list_1)
  print(f'sum: {sum_num}')
  
  average_num = sum_num/len(list_1)
  print(f'average: {average_num}')
  
# call the function below here
stats(example_list)