# Write a program, which will print out for any integer number if it is odd or even.

number = int(input('Please enter a number:\n'))
if number == 0:
    print('Invalid number!')
elif number % 2 == 0:
    print('This number is EVEN')
else:
    print('This number is ODD')