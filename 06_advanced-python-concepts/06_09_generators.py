# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

def my_generator():
    yield 3
    yield "THree"

gen = my_generator()

for value in gen:
    print(value)