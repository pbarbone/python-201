# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def greet(name):
    return f"Hello {name}!"

def write_letter(name, text):
    return f"{greet(name)}\n{text}\nGoodbye {name}!"

def write_letter_to_all(names, text):
    letter = ""
    for name in names:
        letter += write_letter(name, text) + "\n\n"
    return letter

print(write_letter_to_all(["Paolo", "Michele", "Anna"], "I hope this letter finds you well."))