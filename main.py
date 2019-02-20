import sys

class Operation:
	def __init__(self, operation, numbers):
		self.operation = operation;
		self.numbers = numbers;

def introduction():
	print("=== PYTHON CALCULATOR ===\n\n")

def print_instructions():
	instructions = "Type your command in this format: "
	instructions += "add 1,2\n"
	instructions += "Possible operations: add, subtract, multiply, divide\n"
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
	user_input_numbers_int = []
	# ["30", "50"]
	for number in user_input_numbers:
		user_input_numbers_int.append(int(number))
	# [30, 50]

# Create instance of operation class & return it
	operation = Operation(user_input_parsed[0], user_input_numbers_int)
	return operation

def run_operation(task):
	if task.operation == "add":
		# Set a variable for the final answer
		answer = task.numbers[0]
		numbers = task.numbers[1:]
		# Loop through numbers list
		for number in numbers:
			answer += number
		return answer
		# Add it to the final answer

	if task.operation == "subtract":
		answer = task.numbers[0]
		numbers = task.numbers[1:]
		for number in numbers:
			answer -= number
		return answer

	if task.operation == "multiply":
		answer = task.numbers[0]
		numbers = task.numbers[1:]
		for number in numbers:
				answer *= number
		return answer

	if task.operation == "divide":
		answer = task.numbers[0]
		numbers = task.numbers[1:]
		for number in numbers:
				answer /= number
		return answer

def answer_user(solution):
	answer = "\nYour answer is: "
	answer += str(solution)
	answer += "\n"
	print(answer)

def ask_again():
	again = input("Would you like to enter another commmand?: ").lower()
	# If yes, return true
	if again[0] == "y":
		return True
	if again[0] == "n":
		sys.exit()
	# If no, return false

def main():

	while True:
		introduction()
		print_instructions()
		user_input = get_user_input()
		operation = parse_input(user_input)
		answer = run_operation(operation)
		answer_user(answer)
		ask_again()


main()
