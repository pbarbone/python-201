# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

#print("Enter how many random numbers you want to generate: ")
#num = int(input())

random_list = randlist

largest = max(random_list)

print(random_list)
print(f"The largest number in the list is: {largest}")

#find the product of all the numbers in the list
product = 1
for num in random_list:
    product *= num

print(f"The product of all the numbers in the list is: {product}")