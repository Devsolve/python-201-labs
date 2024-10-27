# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

current_set = set()
user_point = 0
print(user_point)
print(current_set)
i = 1
while True:
     current_input = int(input("Enter a number: "))
     if current_input in current_set:
          if user_point!=0:
               user_point -= 1
               print("Number is already present in Set. You lost 1 point")
               if user_point == 5:
                    print("You loose")
                    break    
     else:
          current_set.add(current_input)
          user_point += 1
          print("Right guess, You got 1 point")
          if len(current_set)>= 10:
               print("You win")
               break
     
     

