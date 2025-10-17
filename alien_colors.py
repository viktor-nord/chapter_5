alien_color = 'green'
print('#1')
if alien_color == 'green':
    print("You just earned 5 points!")

if alien_color == 'yellow':
    print("You are yellow!")

if alien_color != 'yellow':
    print("You are not yellow!")

print('#2')
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

if alien_color == 'green':
    print("You just earned 5 points!")
if alien_color != 'green':
    print("You just earned 10 points!")

print('#3')
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
