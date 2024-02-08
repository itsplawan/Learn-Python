import random

to_guess = random.randrange(1,6)
print(f'This is a simple python script that takes your input and compares it with a dice roll and checks if you guessed the roll correctly.')

stopped = False

while not stopped:
    # This takes input from the user.
    usr_guess = input("Enter your guess: ")
    # print(to_guess) #If you want to know what the game is guessing, remove the "#" symbol at the start of this line.

    if int(to_guess) == int(usr_guess):
        choice = input(f'You guessed correctly. Do you want to try again? (Y)es/(N)o: ')
    else:
        choice = input(f'You guessed incorrectly. Do you want to try again? (Y)es/(N)o: ')
        
        if choice.upper() == "Y":
                stopped = False
        elif choice.upper !="Y":
              stopped = True
              break
