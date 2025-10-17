age = 18
print(age == 18)

number = 17
if number != 42:
    print("wrong")

age_1 = 22
age_2 = 18
print(age_1 >= 21 and age_2 >= 21)
age_2 = 22
print(age_1 >= 21 and age_2 >= 21)
print(
    (age_1 >= 21) and 
    (age_2 >= 21)
)

print("-----")

age_1 = 22
age_2 = 18
print(age_1 >= 21 or age_2 >= 21)
age_1 = 18
print(age_1 >= 21 or age_2 >= 21)

print("-----")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
