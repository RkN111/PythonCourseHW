Weight = int('54')
Height = float('1.70')
BMI = round((Weight / (Height*Height)),2)
if BMI <=18.5:
    print (f'Your BMI is: {BMI}\nYou are considered underweight.')
if BMI >18.5 and BMI<=24.9:
    print (f'Your BMI is: {BMI}\nYou are considered normal weight.')
if BMI >=25 and BMI<=29.9:
    print (f'Your BMI is: {BMI}\nYou are considered overweight.')
if BMI >=30:
    print (f'Your BMI is: {BMI}\nYou are considered obese.')