from random import randint



def main():
    p1 = input("Enter player 1's name:\n")
    p2 = input("Enter player 2's name:\n")

    roll1 = rollDice()
    roll2 = rollDice()

    print(p1, 'rolled', roll1)
    print(p2, 'rolled', roll2)

    if roll1 > roll2:
        print(p1, 'WINS!')
    elif roll2 > roll1:
        print(p2, 'WINS')
    else:
        print("It's a tie")

def rollDice():
    return randint(1,6) + randint(1,6)

main()