store_dict = {
	"laptop":{"price":1200, "quantity":5},
	"headphones":{"price":15000, "quantity":10},
	"mouse":{"price":400, "quantity":20}
}

def start():
	while True:
		print('''  
	Welcome To The Online Store Inventory
1. Add a product
2. Update Stock of Existing product
3. Sell Product
4. Display store items
5. Most expensive product
6. Total Potential sales
7. Exit	

''')
		user_choice=int(input("Please enter number to perform task: "))
		call_function(user_choice)

def call_function(choice):
	if choice == 1:
		name=input("Please enter the name of the product: ").lower()
		price=float(input("Enter Price: "))
		quantity=int(input("Enter Quantity: "))
		add_product(store_dict, name, price, quantity)

	elif choice == 2:
		name=input("Please enter the name of the product: ").lower()
		quantity=int(input("Enter Updated Quantity: "))
		update_stock(store_dict, name, quantity)
	
	elif choice == 3:
		name=input("Please enter the name of the product: ").lower()
		quantity=int(input("Enter Quantity you want to sell: "))
		sell_product(store_dict, name, quantity)
	
	elif choice == 4:
		display_inventory(store_dict)

	elif choice == 5:
		most_expensive_product(store_dict)

	elif choice == 6:
		total_potential_sales(store_dict)

	elif choice == 7:
		exit_program()	

	else:
		print("Invalid Input")			

def add_product(store_dict, name, price, quantity):
	if name not in store_dict:
		if len(name)==0:
			print("Product name cannot be empty")
			
		elif price > 0 and quantity > 0:
			store_dict[name]={"price":price, "quantity":quantity}
			print("Added successfully!!")
			print(store_dict)
		else:
			print("Price and quantity must be more than zero")	
	else:
		print("This product already exists.")

def update_stock(store_dict, name, quantity):
	if name in store_dict:
		if quantity > 0:
			store_dict[name].update({"quantity":quantity})
			print("Updated Successfully")
			print(store_dict)
		else:
			print("Quantity should be more than zero")	

	else:
		print("Product does not exist")	
	

def sell_product(store_dict, name, quantity):
	if name in store_dict:
		if quantity > 0:
			product=store_dict[name]
			available_quantity=product["quantity"]
			available_price=product["price"]
			if quantity<=available_quantity:
				available_quantity-=quantity
				store_dict[name].update({"quantity":available_quantity})
				total_sale=quantity*available_price
				print(f"The total sale price is {total_sale}")
				print("Product sold successfully")

				print(store_dict)

			else:
				print("Insufficient stock")
		else:
			print("Quantity should be more than zero")		

	else:
		print("Product does not exist.")		

		
def display_inventory(store_dict):
	total_products=0
	for product, details in store_dict.items():
		total_products+=1
		print(f"{product}: Price is {details['price']}, Quantity is {details['quantity']}")
	print(f"The total number of product is {total_products}"	)


def most_expensive_product(store_dict):	
	most_expensive=0
	prod=None
	for product, details in store_dict.items():
		if details["price"]>most_expensive:
			most_expensive=details["price"]	
			prod=product
			
	print(f"The most expensive product is {prod}, its price is {most_expensive}")	


def total_potential_sales(store_dict):
	total=0
	for product, details in store_dict.items():
		total_each=details["quantity"]*details["price"]
		total+=total_each
	print(f"The value of all the remaining stock is: {total}")	

def exit_program():
	print("Exiting...")
	exit()


start()
	


