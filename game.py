import time
choice = input("Would you like to play a game of adventure (y/n): ")
if choice == "y":
    choice = input(" You are in a dark room and there is 2 doors in front of you. choose right or left (r/l): ")
    if choice == "l":
        choice = input(" you choose the wrong door but you still have a chance to servive choose between door (l/r): ")
        if choice == "l":
            print("You lost, behind these door there was a lion")
        else:
            print('Congratulations champion! You are now free.')
            
    else:
        choice = input("You choose the correct door. Would you like to go to the another door that found in these room (y/n): ")
        if choice == "y":
            print("Congratulations champion! You are now free.")
        else:
            print("sorry the fan droped on your head and you died")
else:
    print("Bye!")
