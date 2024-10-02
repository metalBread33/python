from addAcronym import addAcronym

def findAcronym():
    look_up = input("What acronym would you like to look up?\n")
    found = False
    try:
        with open('demos/acronymsDemo/acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break

    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print ('Acronym does not exist')


def parseInput(choice):
    try:
        if int(choice) == 1:
            findAcronym()
        elif int(choice) == 2:
            addAcronym()
        else:
            print("invalid menu option")
    except:
        print("I'm sorry I don't understand")

def main():
    choice = input('Would you like to find or add an acronym\n1) Find\n2) Add\n')
    parseInput(choice)

main()