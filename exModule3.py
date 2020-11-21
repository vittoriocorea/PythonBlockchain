# Create a list of names and use a for loop to output the length of each name (len() ).

namesList = ['Nicola', 'Marco', 'Max']

def counter1(namesList):
    for name in namesList:
        print(name)
        print(len(name))
    print('-' * 30)

counter1(namesList)


# Add an if  check inside the loop to only output names longer than 5 characters.

def counter2(namesList):
    for name in namesList:
        if len(name) >= 5:
            print(name)
            print(len(name))
    print('-' * 30)

counter2(namesList)


# Add another if  check to see whether a name includes a “n”  or “N”  character.

def counter3(namesList):
    for name in namesList:
        if len(name) >= 5 and ('N' in name or 'n' in name):
            print(name)
            print(len(name))
    print('-' * 30)

counter3(namesList)


# Use a while  loop to empty the list of names (via pop() )

def counter4(namesList):
    while len(namesList) >= 1:     
        print(namesList.pop())
    print(namesList)
    print('-' * 30)

counter4(namesList)


