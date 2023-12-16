# My pizza your pizzas 4.11

pizzas = ["cheese", "jalapeno", "black olives"]
friends_pizzas = pizzas[:]

pizzas.append("banana peppers")
friends_pizzas.append("pepperoni")

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("my friend's favortie pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)