import sys

class Operation:
	def __init__(self, operation, numbers):
		self.operation = operation;
		self.numbers = numbers;

def introduction():
	print("Python Calculator")

def print_instructions():
	instructions = "Type your command in this format: "
	instructions += " add 1,2 "
	instructions += "Possible operations: add, subtract, multiply, divide"
	print(instructions)

def get_user_input():
	user_input = input("Enter your command: ")
	return user_input

def parse_input(user_input):
# add 30,50 ---> 80
# ^ Op. ^Num. list
# ["a","b","c"] <-- List

# Split string into op. and numbers
	user_input_parsed = user_input.split(" ")
	# ["add", "30,50"]
# Make list of numbers (that is easy to work with)
	user_input_numbers = user_input_parsed[1].split(",")
	# ["30", "50"]
	for number in user_input_numbers:
		number = int(number)
	# [30, 50]

# Create instance of operation class & return it
	operation = Operation(user_input_parsed[0], user_input_numbers)
	return operation

def run_operation(operation):
	pass

def answer_user(answer):
	pass

def ask_again():
	pass

def main():
	pass


# main()
user_input = get_user_input()
operation = parse_input(user_input)
print(operation.numbers)