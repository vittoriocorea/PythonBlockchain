# Create two variables - one with your name and one with your age
name = str(input('Enter your name: '))
age = int(input('Enter your age: '))

# Create a function that prints your data as one string
def prints_data():
    """ Prints the name and age as one string. """
    print('My name is ' + name + ' and I am ' + age)


prints_data()

# Create a function that prints ANY data (two arguments) as one string
def prints_ANY_data(var1, var2):
    """ Prints ANY data as one strings.

    Arguments:
        :var1: random variable.
        :var2: random variable. """
    print(var1 + " - " + var2)


prints_ANY_data(name, age)

# Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def calculate_decades(age):
    """ Calculate the decades that you already lived.

    Arguments:
        :age: The number of the years that you lived. """
    decades = age // 10
    return decades


decades_lived = calculate_decades(int(age))
print(decades_lived)





