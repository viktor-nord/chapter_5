requested_topping = ['mushrooms', 'extra cheese']

if "mushrooms" in requested_topping:
    print("adding mushrooms")
if "pepperoni" in requested_topping:
    print("adding pepperoni")
if "extra cheese" in requested_topping:
    print("adding extra cheese")

print("-----")

if "mushrooms" in requested_topping:
    print("adding mushrooms")
elif "pepperoni" in requested_topping:
    print("adding pepperoni")
elif "extra cheese" in requested_topping:
    print("adding extra cheese")

for val in requested_topping:
    if val == "mushrooms":
        print("sorry, no mushrooms available")
    else:
        print(f"adding {val} to pizza")

print("-----")

empty_list = []
if empty_list:
    for val in empty_list:
        print("This won't print because the list is empty.")
else:
    print("No toppings!")