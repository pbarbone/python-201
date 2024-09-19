# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1. Convert to a different data type
# convert the list to a set
set_ = set(list_)
# convert the set back to a list
list_ = list(set_)
print(list_)

# 2. Use a loop and a second list to solve it more manually
# create a new list
new_list = []
# iterate over the original list
for item in list_:
    # if the item is not in the new list
    if item not in new_list:
        # add it to the new list
        new_list.append(item)
print(new_list)

