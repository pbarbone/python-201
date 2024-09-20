# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def realtor_ad(**kwargs):
    print("Here's some information about this property:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

realtor_ad(
    location="1935 38th St",
    price="$500,000",
    bedrooms=2,
    bathrooms=2,
    square_feet=1400,
    garage=False
)

