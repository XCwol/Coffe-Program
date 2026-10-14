# Error Checking
# Xander Wolmarans
# 25 Sept 2026

# Code that tests whether a valid input was given (v1)
'''done = True # Boolean variable set to True
while done:
    num = int(input("Please enter your value as an integer: "))
    done = False

    print(f"The number you entered is {num}")'''
    
# Using a try and except method to check for valid input (v1.1)
# Use try and except method to catch errors
done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True
        
    except ValueError:
        print("This is not a valid number. \nUse a fullstop as a decimal indicator\n")

print(f"The number you entered was {num}.")

