# PythonBlockchain
# Initializing your blockchain
blockchain = []


def get_last_blockchain_value():
	""" Returns the last value of the current blockchain. """
	if len(blockchain) < 1:
		return None
	return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
	""" Appends a new values as well as the last blockchain value to the blockchain

	Arguments:
		:transaction_amount: The amount that should be added.
		:last_transaction: The last blockchain transaction (as default [1])"""
	if last_transaction == None:
		last_transaction = [1]
	blockchain.append([last_transaction,transaction_amount])


def get_transaction_value():
	""" Returns the input of the user (a new transaction amount) as a float. """
	# Get the user input, transform it from a string to a float and store it
	user_input = float(input('Your transaction amount: '))
	return user_input


def get_user_choice():
	""" Returns the choose of the user (ex. "1" )"""
	user_input = input('Your choose: ')
	return user_input


def print_blockchain_elements():
	""" Returns the output of the blockchain"""
	# Print the Blockchain list to the console
	for block in blockchain:
		print('Outputting block...')
		print(block)
	else:
		print('_' * 20)


def verify_chain():
	""" Returns True or False. It verifies if the blockchain was manipulate"""
	is_valid = True
	for block_index in range(len(blockchain)):
			if block_index == 0:
				continue
			elif blockchain[block_index][0] == blockchain[block_index - 1]:
				is_valid = True
			else:
				is_valid = False
				break

	return is_valid

waiting_for_input = True

while True:
	print('Please choose')
	print('1: Add a new value to the blockchain list')
	print('2: Print the blockchain list')
	print('h: Manipulate the chain')
	print('q: Quit')
	user_choice = get_user_choice()
	if user_choice == '1':
		tx_amount = get_transaction_value()
		add_transaction(tx_amount, get_last_blockchain_value())
	elif user_choice == '2':
		print_blockchain_elements()
	elif user_choice == 'h':
		if len(blockchain) >= 1:
			blockchain[0] = [2]
	elif user_choice == 'q':
		waiting_for_input = False
	else:
		print('Input was invalid, please choose a value from the list')
	if verify_chain() == False:
		print_blockchain_elements()
		print('Invalid blockchain!')
		break

else:
	print('User left!')

print('Done!')
