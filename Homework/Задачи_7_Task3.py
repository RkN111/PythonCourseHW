# Задача 3. Да се създаде програма, която чете думи като вход от клавиатурата, докато
# потребителят не въведе празен ред. След като потребителят въведе празен ред,
# програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
# Думите трябва да се показват в същия ред, в който са били въведени. Например, ако
# потребителят въведе:
# first
# second
# first
# third
# second

word_list = []
list_wthout_duplicates = []
while True:
    user_input = input('Please enter a word:')
    if user_input == '':
         break
    word_list.append(user_input)
for i in word_list:
     if i not in list_wthout_duplicates:
            list_wthout_duplicates.append(i)
for i in list_wthout_duplicates:
     print(i)           
# print (list_wthout_duplicates)