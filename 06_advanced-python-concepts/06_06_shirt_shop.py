# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

cartesian_product = [(color, size) for color in colors for size in sizes]

for item in cartesian_product:
    print(item)