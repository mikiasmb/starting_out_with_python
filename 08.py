import pickle
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def veg():
	pass


def main():
	vegetables = dict()
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
		while LOOK_UP > choice or choice > DELETE:
			choice = int(input("Enter a valid choice: "))
	except ValueError:
		choice = int(input("Enter a valid choice: "))
	return choice
	

def look_up(vegetable):
	for vegi, price in vegetable.items():
		print(f"{vegi}: ${price}")
		
		
def add(vegetable):
	vegi = input("Enter a vegetable: ")
	price = float(input("Enter the price: "))
	if vegi not in vegetable:
		vegetable[vegi] = price
	else:
		print(f"{vegi} already exists.")


def change(vegetable):
	vegi = input("Enter a vegetable: ")
	if vegi in vegetable:
		price = float(input("Enter the price: "))
	else:
		print(f"{veg} is not in the list.")


def delete(vegetable):
	vegi = input("Enter a vegetable: ")
	if vegi in vegetable:
		del vegetable[vegi]
	else:
		print(f"{vegi} is not in the list.")
		
		
if __name__ == '__main__':
	main()
