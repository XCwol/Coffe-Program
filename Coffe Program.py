# Creating a coffe program that a user will 
# able to interact with 
# Xander Wolarans
# 23 Sept 2026
# Version 1

# TODO: record an input (Store the answer)
#       check for valid answer (input checker)
#       Ask questions to respond

# Ask the user whether they like coffe or not
like_coffe = input("Do you like coffe? ")
# print(like_coffe) # checking that the input is stored
print(f"Your answer was '{like_coffe}'.")

# Check the input and respond
if like_coffe == "Yes" or like_coffe == "yes" or like_coffe == "Y" or like_coffe == "y": # to be fixed next time
    print("Thank is great! I like coffe too.") 
else:
    print("You are missing out! Why not give it a try?")