
# Ask the user for a number

'''number = float(input("Enter a number: "))

# Check whether it's negative, positive, or zero
if number < 0:
    print("negative")
if number > 0:
    print("positive")
if number == 0:
    print("zero")

if number >= 1000:
        print("very large integer")
if number <= -1000:
        print("very small integer")
'''

'''
number = int(input("Enter an integer: "))

# Check only for very large or very small
if number >= 1000:
    print("very large integer")
elif number <= -1000:
    print("very small integer")'''
# Ask the user for a number
number = int(input("Enter an integer: "))

# Check the conditions
if number >= 1000:
    print("very large integer")
elif number <= -1000:
    print("very small integer")
else:
    print("normal integer")
