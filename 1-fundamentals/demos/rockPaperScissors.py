from random import randint #gets only the randint func

computerChoice = randint(1,3)
userChoice = int(input('Rock, paper, or scissors? \n1) Rock\n2) Paper \n3) Scissors\n'))

if computerChoice == userChoice:
    print("TIE")
elif userChoice == 1 and computerChoice == 3:
    print("YOU WIN!")
elif userChoice == 3 and computerChoice == 1:
    print("YOU WIN!")
elif userChoice == 2 and computerChoice == 1 :
    print("YOU WIN!")
else: 
    print("You lose :(")