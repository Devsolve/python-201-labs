# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name,*message):
     letter = ""
     for m in message:
          l_msg = f"{m} {name}!"
          letter+=l_msg
     return letter

letter = write_letter('Arun', "Good Morning", "Goodbye")
print(letter)