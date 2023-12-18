# No pastrami 7.9

sandwich_orders = ['bologna', 'pastrami', 'peanut butter', 'pastrami', 'turkey breast', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami")

# Loop removing pastrami from list

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
# Looping through sandwich orders
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich")

    # Appending sandwiches to finished sandwiches list

    finished_sandwiches.append(sandwich)
    print(f"The following {sandwich} sandwich was made")
