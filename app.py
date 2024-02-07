import os, random, time, colorama, sys ## Importing needed libraries.
from colorama import Fore as F
from colorama import Back as B
colorama.init(autoreset=True) ## Resets line color to default each line. Makes coloring text easier. ##

'''
Code Scheme / Idea

Make a dice game that the player can roll 2 dice and combine the score.

If the score is 7 or 11 the player wins, if its 2, 3, or 12 the player loses, if none of them occur, repeat the round.

Criteria:
*The user should be displayed different information like the round status with print functions.
*The user should be able to select between re rolling or ending the game.

'''
### FUNCTIONS ###
def roll_dice():
    dice1 = random.randint(1, 6) ## Gives a random value from 1 to 6 to the dices. ##
    dice2 = random.randint(1, 6)

    selection = input("Write R to roll dices. Write Q to quit. > ").upper().strip() 
    print()
    
    if selection == "R":
        print("Rolling a dice...")
        time.sleep(2)
        print(f"You rolled a {F.CYAN}{dice1}!")
        time.sleep(2)
        print("Rolling next dice...")
        time.sleep(2)
        print(f"You rolled a {F.CYAN}{dice2}!")
        
        if dice1 == dice2:
            print(f"{F.CYAN}Its a pair!")
    
    elif selection == "Q":
        os.system('clear')
        print(f"{F.RED}Closing Game...")
        sys.exit("Goodbye!")
        
    return dice1 + dice2 ## Returns dice score ##

def checkscore(score):
    if score == 7 or score == 11:
        os.system('clear')
        print(f"{F.GREEN}You win! Your dice score was: {score}")
        gameover = True
        
    elif score == 2 or score == 3 or score == 12:
        os.system('clear')
        print(f"{F.RED}You Lose. Your dice score was: {score}")
        gameover = True
    
    else:
        print(f"The score was {score}, the game will continue.\n")

### CODE ###
gameover = False

print(f"{F.BLUE}Angel's Dice Game")
user_name = input(f"Welcome to the game, what is your name? > ")
print("\nIf your score is 7 or 11, you win,\nIf its 2, 3, or 12 you lose,\nOtherwise you can keep rolling.")
time.sleep(5)
os.system('clear')

while not gameover:
    if user_name == "konami":
        print("You win due to an easter egg.")
        break
    
    score = roll_dice()
    checkscore(score)