from random import randint

def roll_the_dice(num_of_faces):    
    return randint(1, num_of_faces)

result = 0
print("------ Rolling Dice Simulator ------\n"
    "Please enter the number of faces from the dice: ")
