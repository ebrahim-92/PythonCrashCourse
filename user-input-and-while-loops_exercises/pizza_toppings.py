# Pizza toppings 7.4

toppings = "\nPlease enter your requested toppings: "
toppings += "\n(Enter 'quit' to stop requesting toppings)"
final_order = ""

# Loop to handle toppings

while final_order != 'quit':
    final_order = input(toppings)

    if final_order != 'quit':
        print(f"Adding {final_order}")
    
    if final_order == 'quit':
        print("")