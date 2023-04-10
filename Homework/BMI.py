Weight = int(54.3)
Height = float(170)
BMI = round((Weight / (Height*Height)),2)
print(BMI)
# try:
#     Weight = int(input('Please enter your weight in kg: '))
#     Height = float(input('Please enter your height in meters: '))
#     BMI= round((Weight / (Height*Height)),2)
#     print(BMI)
# except ValueError:
#     print('Wrong input, please enter a number!')
# except 