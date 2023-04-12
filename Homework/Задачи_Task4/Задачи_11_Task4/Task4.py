# Задача 4. Създаване на калкулатор, който да може да пресмята събиране,
# умножение, деление и изваждане. Да се създаде модул calculator, който да съдържа
# функциите add, subtract, multiplication, division. Да се създаде и друг модул, в който
# да се извикат тези функции, модулът да се казва task2_calculation.py. Да се накара
# потребителят да въведе двете числа. Модулът calculator.py да има и функция за
# принтиране на резултата.



import calculator
while True:
    try:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        break
    except:
        print('Invalid input!')
while True:
    try:
        c = int(input('''Now, choose which operation to perform.
    To add (+), press 1
    To substract (-), press 2
    To multiplicate (*), press 3
    To divide (/), press 4
    :'''))
        break
    except:
        print('Invalid operation!')
if c == 1:
    print(calculator.add(a,b))
elif c == 2:
    print(calculator.substract(a,b)) 
elif c == 3:
    print(calculator.multiplication(a,b))
elif c == 4:
    print(calculator.division(a,b))
    