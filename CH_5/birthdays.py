birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    name = name.capitalize()
    if name == '':
        break

    if name != '':
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have the birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            bday = bday.capitalize()
            birthdays[name] = bday
            print('Birthday database updated.')