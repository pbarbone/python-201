# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

# open the file
with open('words.txt', 'r') as file:
    # read the file
    words = file.read().split()
    # create a list of the lengths of the words
    word_lengths = [len(word) for word in words]
    # shortest word
    shortest_word = min(word_lengths)
    # longest word
    longest_word = max(word_lengths)
    # create a list of the shortest words
    shortest_words = [word for word in words if len(word) == shortest_word]
    # create a list of the longest words
    longest_words = [word for word in words if len(word) == longest_word]
    # find the total number of words
    total_words = len(words)

print(f"The shortest word(s) is/are: {shortest_words}")
print(f"The longest word(s) is/are: {longest_words}")
