# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).


loong_words = []
# open the file
with open('words.txt', 'r') as file:
    # read the file
    words = file.read().split()
    # iterate over the words
    for word in words:
        # if the length of the word is greater than 20
        if len(word) > 20:
            # print the word
            loong_words.append(word)

print(loong_words)
