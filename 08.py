import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILE_NAME = "Vegetables.dat"


def main():
	vegetables = load_vegetables()
	choice = 0
	
	while choice != QUIT:
		choice = menu()
		
		if choice == LOOK_UP:
			look_up(vegetables)
		elif choice == ADD:
			add(vegetables)
		elif choice == CHANGE:
			change(vegetables)
		elif choice == DELETE:
			delete(vegetables)
	save_vegetables(vegetables)


def load_vegetables():
	try:
		with open(FILE_NAME, "rb") as file:
			vegetables = pickle.load(file)
	except FileNotFoundError:
		vegetables = {}
	return vegetables
	

def save_vegetables(vegi):
	with open(FILE_NAME, "wb") as file:
		pickle.dump(vegi, file)
	
	
def menu():
	print()
	print("""1. Look up the vegetables and prices.
2. Add a vegetable and price.
3. Change a vegetable price.
4. Delete a vegetable and price.
5. Quit.""")
	print()
	try:
		choice = int(input("Enter your choice: "))
		while choice < LOOK_UP or choice > QUIT:
			choice = int(input("Enter a valid choice: "))
	except ValueError:
		choice = 0
	return choice
	

def look_up(vegetable):
	for vegi, price in vegetable.items():
		print(f"{vegi.captalize()}: ${price:,.2f}")
		
		
def add(vegetable):
	vegi = input("Enter a vegetable: ").capitalize()
	try:
		price = float(input("Enter the price: "))
		if vegi not in vegetable:
			vegetable[vegi] = price
		else:
			print(f"{vegi} already exists.")
	except ValueError:
		print("Error! Invalid price please enter a valid price.")
	

def change(vegetable):
	vegi = input("Enter a vegetable: ").capitalize()
	try:
		if vegi in vegetable:
			price = float(input("Enter the price: "))
			vegetable[vegi] = price
		else:
			print(f"{vegi} is not in the list.")
	except ValueError:
		print("Error! Invalid input please enter a valid price.")


def delete(vegetable):
	vegi = input("Enter a vegetable: ").capitalize()
	if vegi in vegetable:
		del vegetable[vegi]
	else:
		print(f"{vegi} is not in the list.")
		
		
if __name__ == '__main__':
	main()
