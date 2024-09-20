# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divis_four_seven(number):
    return number % 4 == 0 or number % 7 == 0

def divis_four_seven_both(number):
    return number % 4 == 0 and number % 7 == 0

user_input = int(input("Enter a number between 1 and 1,000,000,000: "))
result_one = divis_four_seven(user_input)
result_two = divis_four_seven_both(user_input)

print(f"Is {user_input} divisible by 4 or 7? {result_one}")
print(f"Is {user_input} divisible by both 4 and 7? {result_two}")
