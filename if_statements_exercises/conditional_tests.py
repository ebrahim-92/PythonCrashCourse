# Conditional tests 5.1, only will test two variables not ten like requested

food = ["rice", "chicken", "fish"]
favorite_food = "biryani"
second_favoritefood = "chicken"

if favorite_food in food:
    print("We can serve you your requested dish")
else:
    print(f"\nSorry we are out of {favorite_food}")

if second_favoritefood in food:
        print("We can serve you your requested dish")
else:
    print(f"\nSorry we are out of {favorite_food}")

