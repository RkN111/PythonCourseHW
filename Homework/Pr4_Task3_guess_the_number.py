
# Write a simple Python program, implementing the "Guess the number" game, following the rules:
#     The program will "think" of a number using the random module, as shown in code shown in next slide.
# You have to implement now only the first user move:
#     Prompt the user for his/her guess
#     If the user guess is equal to the machine number => print out a congratulation message!
#     If the user guess is less than the machine number => print out "your guess is less than my number. Try again!"
#     If the user guess is greater than the machine number => print out "your guess is greater than my number. 
#     Try again!" 
# personal note: Понеже като тествах играта и постоянно губех, нямаше как да разбера дали всичко работи както трябва.
# Затова накарах играта да ми казва какъв е бил номера за да знам със сигурност, че кода работи адекватно.

print ('*'*28 +'\nWelcome to Guess the Number!\n'+'*'*28)
print ('In this game you have to guess a random number ranging from 1 to 10.')
import random
random_number = random.randint(1,10)
user_number = int(input('Please type in your number: '))
if user_number == random_number:
    print ("Congratulations! You win!")
elif user_number > random_number:
    print (f'Your guess is less than my number. Try again! My number was {random_number}.')
else: print (f'Your guess is greater than my number. Try again! My number was {random_number}.')
