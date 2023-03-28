# Задача 3. Да се създаде речник, който да съдържа информацията за дадено меню на
# ресторант. Ключовете му трябва да са стрингове, а стойностите цените. Програмата ще
# по иска от потребителя да въведе следната информация:
# - Ако потребителят въведе името на дадено ястие от менюто, тогава програмата
# да принтира цената и колко е общата цена до момента. След това да пита
# отново дали потребителят не иска да въведе нещо друго.
# - Ако потребителят въведе име на ястие, което не е в менюто, тогава програмата
# да изведе подходящо съобщение. След което отново програмата да пита
# потребителя да избере нещо друго от менюто.
# - Ако потребителят въведе празен стринг, тогава програмата да спре да подканва
# потребителя да избира от менюто и да изведе на екрана общата крайна сума.
# Пример:
# Order: sandwich
# sandwich costs 10, total is 10
# Order: tea
# tea costs 7, total is 17
# Order: elephant
# Sorry, we are fresh out of elephant today. Order: <enter>
# Your total is 17

menu = {'Salad':3.50,
        "Tarator":2.00,
        'Kebapche':2.50,
        'Rakia':3.00,
        'Bread':0.50,
        'Banitsa':4.99,
        'Sarma':5.00}
total = []
print ('Welcome to our resturant, please type in order.\nPress Enter to finish.\n')
while True:
    user_order = input('Enter your order: ')
    order_price = menu.get(user_order)
    if user_order == '':
        break
    if user_order in menu:
        total.append(order_price)
        print(f'Order: {user_order}\n{user_order} costs {order_price}, total is {round(sum(total),2)}') 
    else:
        print('Sorry, we don\'t have that at the moment.')
    
print(f'Your total is: {round(sum(total),2)}')
# Добавих round() защото като го тестах в един момент ми излезе това като обща сметка:
# Order: Rakia
# Rakia costs 3.0, total is 18.990000000000002
