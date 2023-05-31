def user_attack():
    while(True):
        try:
            print("Select your attack:\nPunch: 1\nKick: 2")
            atk = int(input())
            if(atk == 1 or atk == 2):
                return atk
            else:
                print("Please choose between 1 and 2")
        except ValueError:
            print("Please choose between 1 and 2")
        except:
            print("Something went wrong")

def user_defence():
    try:
        while(True):
            print("Select your defence:\nHigh: 1\nLow: 2")
            dfc = int(input())
            if(dfc == 1 or dfc == 2):
                return dfc
            else:
                print("Please choose between 1 and 2")
    except ValueError:
        print("Please choose between 1 and 2")
    except:
        print("Something went wrong")

