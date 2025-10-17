car = 'bmw'
print(car == 'bmw')
print(car != 'bmw')
print('b' in car)
print('B' in car)
print('B' not in car)
print('b' not in car)
print('long word' > car)
print('b' > car)
print(car.upper() == 'BMW' and car.title() == 'Bmw')
print(car.upper() == 'BMW' and car.title() == 'bmw')
print('BMW'.lower() == car)

print('numbers:')

first_number = 1
second_number = 1337
print(first_number < second_number)
print(first_number > second_number)
print(first_number <= second_number)
print(first_number >= second_number)
print(first_number <= 1)
print(first_number >= 1)
print(first_number < second_number and first_number > second_number)
print(first_number < second_number or first_number > second_number)

list = list(range(5))
print(first_number in list)
print(first_number not in list)
