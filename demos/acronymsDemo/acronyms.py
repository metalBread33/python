
look_up = input("What acronym would you like to look up?\n")
found = False
with open('demos/acronymsDemo/acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print ('Acronym does not exist')