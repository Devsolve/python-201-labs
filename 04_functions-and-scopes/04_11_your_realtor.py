# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def real_estate_advertisement(**letter):
     print("Real Estate Advertisement:") 
     print("-------------------------")
     for key, val in letter.items():
          print(f'{key.capitalize()}: {val}')
     print("-------------------------")
     

real_estate_advertisement(
     title="Beautiful 3-bedroom apartment", 
     location="Downtown", 
     price="$500,000", 
     size="1200 sq ft", 
     amenities="Pool, Gym, Parking"
     )