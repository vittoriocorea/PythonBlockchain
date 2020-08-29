# Create a list of names and use a for loop to output the length of each name (len())
names  = ['Max', 'Ralph', 'Piero', 'Pasquale', 'Nicola']


def output_name_len():
    for name in names:
        print(name)
        print(len(name))

output_name_len()

# Add an if  check inside the loop to only output names longer than 5 characters
print('_' * 30)

def output_5_characters():
    for name in names:
        if len(name) >= 5:
            print(name)
            print(len(name))

output_5_characters()

# Add another if  check to see whether a name includes a “n”  or “N”  character
print('_' * 30)

def output_N_names():
    for name in names:
        if len(name) >= 5 and ('n' in name or 'N' in name):
                print(name)
                print(len(name))

output_N_names()

#  Use a while  loop to empty the list of names (via pop())
print('_' * 30)

def empty_list_names():
    while len(names) >= 1:
        print(names.pop())
    print(names)

empty_list_names()