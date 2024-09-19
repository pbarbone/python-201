# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

converted_tuple = tuple(string)

converted_list = list(converted_tuple)

converted_list[0] = "k"

converted_tuple = tuple(converted_list)

print(converted_tuple)
