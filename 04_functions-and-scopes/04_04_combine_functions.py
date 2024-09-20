# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

#assume the greet function takes a name and returns a greeting message
def greet(name):
    return f"Hello {name}!"

def write_letter(name, text):
    return f"{greet(name)}\n{text}\nGoodbye {name}!"

# Test the function

letter = write_letter("Sarah", "I hope this letter finds you well.")

print(letter)