# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


def make_sandwich(bread,*toppings):
     sandwich = f'{bread} sandwich with '
     if toppings:
          sandwich+= ", ".join(toppings)
     else:
          sandwich+= "no toppings"
     sandwich += f" between {bread} slices."
     return sandwich

print(make_sandwich("whole wheat", "lettuce", "tomato", "turkey"))