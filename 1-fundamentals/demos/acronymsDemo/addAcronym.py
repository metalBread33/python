
def addAcronym():
    acronym = input('What acronym would you like to add\n')
    definition = input('What is the definition?\n')

    with open('demos/acronymsDemo/acronyms.txt', 'a') as file: #a param allows us to append to file
        file.write('\n' + acronym + ' - ' +  definition)