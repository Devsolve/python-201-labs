# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def check_divisible(divisible_num):
     if divisible_num % 4 == 0 and divisible_num % 7 == 0:
          return True
     else: return False
     
user_input = int(input("Enter a number: "))
answer = check_divisible(user_input)
print(answer)