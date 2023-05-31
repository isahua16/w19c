from input_handler import user_attack
from input_handler import user_defence
import random

def game_loop():
    print("Welcome to Mortal Kombat!")
    user_health = 100
    computer_health = 100
    while(user_health > 0 or computer_health > 0):
        user_atk = user_attack()
        user_dfc = user_defence()
        computer_atk = random.randint(1,2)
        computer_dfc = random.randint(1,2)
        if((user_atk == 1 and computer_dfc == 2) or (user_atk == 2 and computer_dfc == 1)):
            computer_health = computer_health - 10;
        elif((computer_atk == 1 and user_dfc == 2) or (computer_atk == 2 and user_dfc == 1)):
            user_health - 10;
    return

game_loop()

