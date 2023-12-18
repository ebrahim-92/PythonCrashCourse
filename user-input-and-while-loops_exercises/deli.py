# Deli 7.8

sandwich_orders = ['bologna', 'peanut butter', 'turkey breast']
finished_sandwiches = []

# Looping through sandwich orders
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich")

    # Appending sandwiches to finished sandwiches list

    finished_sandwiches.append(sandwich)
    print(f"The following {sandwich} sandwich was made")
