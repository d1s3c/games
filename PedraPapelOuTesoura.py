import random, os, sys

#poss list
lista = ["Rock", "Paper", "Scissors"]

##clear screen
def cls():
    os.system("cls")
##end or continue code
def base(val):
    cont = 0 
    cont_npc = 0
    while True:
        print("{}: {}".format(user, cont))
        print("NPC: {}".format(cont_npc))
        if val == cont or val == cont_npc:
            cls()
            if cont > cont_npc:
                non = input("WINNER: {}!!!!\nPress ENTER to continue...".format(user))
                mod()
            else:
                non = input("WINNER: NPC!!!!\nPress ENTER to continue...")
                mod()
        else:
            pass
        ##structure
        a = input("ROCK | PAPER | SCISSORS: ")
        b = lista[random.randint(0,2)]
        if b.upper() == a.upper():
            print("Draw!!")
            non = input("Press ENTER to continue...")
            cls()
        elif a.upper() == "ROCK" and b.upper() == "SCISSORS":
            print("1 point {} !!".format(user)) 
            cont += 1
            non = input("Press ENTER to continue...")
            cls()
        elif a.upper() == "SCISSORS" and b.upper() == "PAPER":
            print("1 point {} !!".format(user)) 
            cont += 1
            non = input("Press ENTER to continue...")
            cls()
        elif a.upper() == "PAPER" and b.upper() == "ROCK":
            print("1 point {} !!".format(user)) 
            cont += 1
            non = input("Press ENTER to continue...")
            cls()
        else:
            print("1 point NPC !!") 
            cont_npc += 1
            non = input("Press ENTER to continue...")
            cls()
#game mod
def mod():
    cls()
    while True:
        cho = input("Game Mode:\nUntil 5[1]\nUntil 10[2]\nUntil 15[3]\Free[4]\Quit[5]\n--> ")
        if cho == "1":
            cls()
            base(5)
        elif cho == "2":
            cls()
            base(10)
        elif cho == "3":
            cls()
            base(15)
        elif cho == "4":
            cls()
            base(-1)
        elif cho == "5":
            sys.exit()
        else:    
            non = input("Invalid Choice, Press ENTER to continue...")
            cls()
#base
user = input("Player Name: ")
mod()










