# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

# Read in 10 numbers from the user.
numbers = []
for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Print out the second number received, followed by the 4th,

print(numbers[1], numbers[3], numbers[5], numbers[7], numbers[9])

