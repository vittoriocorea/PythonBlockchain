# PythonBlockchain
#
# Initializing your blockchain
blockchain = []


def get_last_blockchain_value():
	""" Returns the last value of the current blockchain. """
	return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
	 """ Appends a new values as well as the last blockchain value to the blockchain

	Arguments:
		:transaction_amount: The amount that should be added.
		:last_transaction: The last blockchain transaction (as default [1])
	"""
	blockchain.append([last_transaction,transaction_amount])


def get_user_input():
	""" Returns the input of the user (a new transaction amount) as a float. """
	return float(input('Your transaction amount: '))

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)