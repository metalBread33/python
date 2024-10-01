contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Sarah', 'email':'sarah@example.com'},
        {'name': 'Harry', 'email': 'harry@example.com'},
        {'name': 'Ron', 'email': 'ron@example.com'}
    ]
}

print('Student emails: ')
for student in contacts['students']:
    print (student['email'])