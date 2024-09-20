# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    return f"Hello {name},\n{text}\nGoodbye {name}!"

# Test the function

letter = write_letter("Sarah", "I hope this letter finds you well.")
print(letter)
# Expected output:
# Hello Sarah,
# I hope this letter finds you well.
# Goodbye Sarah!

