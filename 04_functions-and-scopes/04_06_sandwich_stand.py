# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread_type,*toppings):
    return f"{bread_type} sandwich with {', '.join(toppings)}"

# Test the function

sandwich = make_sandwich("Rye", "Cheese", "Salami", "Tomato", "Lettuce")

print(f"Much delicious very sandwich: {sandwich}")