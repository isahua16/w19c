def user_attack():
    while(True):
        print("Select your attack:\nPunch: 1\nKick: 2")
        atk = int(input())
        if(atk == 1 or atk == 2):
            return atk
        else:
            print("Invalid Attack")

def user_defence():
    while(True):
        print("Select your defence:\nHigh: 1\nLow:2")
        dfc = int(input())
        if(dfc == 1 or dfc == 2):
            return dfc
        else:
            print("Invalid Defence")

