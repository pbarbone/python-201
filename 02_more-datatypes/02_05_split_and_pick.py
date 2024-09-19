# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

# Get user input
text = input("Enter a sentence: ")

# Split the text into a list of words
words = text.split()

# Create a dictionary to store the count of each word
word_count = {}

# Count the number of times each word appears in the list
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    
# Find the most common word
most_common_word = max(word_count, key=word_count.get)

print(f"The most common word in the text is: {most_common_word}")