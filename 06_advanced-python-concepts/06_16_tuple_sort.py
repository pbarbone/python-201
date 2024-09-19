# Use a lambda expression to sort a list of tuples based on
# the number value in the tuple. For example:
#
# unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
# sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

#find just a number in a list of tuples

filtered_tuples = list(filter(lambda tup: any(isinstance(x, (int)) for x in tup), unsorted_list))

print(filtered_tuples)

sorted_tuples = sorted(unsorted_list, key = lambda x: x[1])

print(sorted_tuples)