from input_handler import user_attack
from input_handler import user_defence
import random
import webbrowser

def game_loop():
    print("Welcome to Mortal Kombat!")
    user_health = 20
    computer_health = 20
    while(user_health > 0 and computer_health > 0):
        print("User Health:", user_health)
        print("Computer Health:", computer_health)
        user_atk = user_attack()
        user_dfc = user_defence()
        computer_atk = random.randint(1,2)
        computer_dfc = random.randint(1,2)
        if((user_atk == 1 and computer_dfc == 2) or (user_atk == 2 and computer_dfc == 1)):
            computer_health = computer_health - 10;
            if(computer_health > 0):
                print("You hit the computer for 10 points ✅")
            else:
                print("You win! 🏆")
                webbrowser.open("https://images.unsplash.com/photo-1578269174936-2709b6aeb913?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80")
                return
        else:
            print("Your attack was blocked! ❌")
        if((computer_atk == 1 and user_dfc == 2) or (computer_atk == 2 and user_dfc == 1)):
            user_health = user_health - 10
            if(user_health > 0):
                print("The computer hits you for 10 points 🔻")
            else:
                print("You lose 💀")
                return
        else:
            print("You blocked the computer's attack! ❎")

game_loop()

