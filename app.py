# Imports # 
import os, time, random, colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Data #
player_info = {
    'name': input("Name > "),
    'level': 1,
    'attack': random.randint(25,37),
    'defense': 10,
    'weapon': 'Basic Sword'
}

enemy_names = [
    "Witch", "Giant Spider", "Vampire"
]

enemy_info = {
    'health': 100,
    'defense': random.randint(5, 15),
    'level': 1
}

# Functions #
def typewriter(sentence):
    for char in sentence:
        time.sleep(0.1)
        print(char, end='', flush=True)

# Code #
player_dead = False
turn = 'player'

typewriter("You wake up in a cave, you can't remember how you got there.")


os.system("clear")

try:
    match turn:
        case 'player': 
            pass
        case 'enemy':
            pass

except:
    os.system("clear")
    print(f"{Fore.RED}The app has stopped due to a missing value.")
