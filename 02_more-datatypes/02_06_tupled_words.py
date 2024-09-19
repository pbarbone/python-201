# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

#split the words
separated = input.split()

#iterate over the words and create a tuple for each word
result_list = []

for word in separated:
    result_list.append(tuple(word))

print(result_list)