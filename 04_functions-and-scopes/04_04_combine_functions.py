# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name,*message):
     letter = ""
     for m in message:
          l_msg = greet(m,name)
          letter+=l_msg
     return letter

letter = write_letter('Arun', "Good Morning", "Goodbye")
print(letter)