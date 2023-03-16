# # Задача 1. Принтирайте следният текст на екрана:
# #  “23 4.5 False John”. (don't just copy paste!!! That's not the idea here!!)
# print ('"23 4.5 False John".')
# print ("\"23 4.5 False John\".")

# # Задача 2. Попълнете празните полета, като използвате форматиращият метод format. Празните места запълнете с вашето име и любими активности.

# # ”{ }’s favorite sports is { }.”
# # “{ } is working on { } programming!”
# name = 'Rumi'
# sports = 'E-sports'
# activity = 'learning'
# print ('''{0}\'s favorite sports is {1}.
# {0} is working on {2} programming!'''.format(name,sports,activity))

# print ('%s\'s favorite sports is %s.\n%s is working on %s programming!'%(name,sports,name,activity))

# # Задача 3. Създайте променлива, paragraph, която да съдържа следното съдържание:
# # "Python is a great language!", said Fred. "I don't ever remember having this much fun before. "
# paragraph = '"Python is a great language!", said Fred.\n"I don\'t ever remember having this much fun before.'
# print (paragraph)
# paragraph = "\"Python is a great language!\", said Fred.\n\"I don't ever remember having this much fun before.\""

# # Задача 1. Създайте стринг, който да се казва school 
# # и да съдържа името на вашето училище. Използвате методите, които научихте за да промените стринга. 
# # Ако е необходимо използвайте help функцията.
# school = 'ПГКО Кунино'.replace('ПГКО Кунино','НХГ Цанко Лавренов')
# print ('Завърших от гимназията {}.'.format(school))

# # Задача 2. Създайте стринг, който да се казва country и присвоете на него стойност “usa”.
# # Създайте нов стринг, correct_country, чиято стойност да е държавата само с големи букви,
# # като използвате някой от стринг методите.
# country = 'usa'
# correct_country = country.upper()
# print (f'One day I want to visit the {correct_country}.' )

# # Задача 3. Създайте стринг,  filename и му присвоете стойност “hello.py”.
# # Проверете дали стринга завършва на “.java”. Намерете индексът на ”py”.
# # Проверете и дали думата започва с ”world”.
# filename = 'hello.py'
# print (filename.find('py'))


# # Задача 4. Опитайте се да принтирате стринг изцяло с главни букви.
message = '“Forget about saving, go for the tie!!!”'.upper()
print (message)

# Задача 5. Напишете програма, която да премахва ”$$” от името ”$$John Smith”. Опитайте с .lstrip и .strip(). За да видите описанието на двете функции използвайте следното help(“ ”.strip).
name = '$$John Smith'
print ('{} likes to play basketball on the weekends'.format(name).strip('$$'))
print ('{} likes to play basketball on the weekends'.format(name).lstrip('$$'))

# Задача 6. Да се напише програма, която да принтира информацията от упр. 6 на презентацията 
# (pers. note: around 54 stars and 39 =)+ how do I add the $ sighn without killing it?

store_name = 'Coding Temple, Inc.'
store_address = '283 Franklin St..'
store_state = 'Boston, MA'
border1 = '*'*40
border2 = '='*40
product_info = 'Item'
product_price = 'Price'
item1 = 'Books'
item1_price = 49.55
item2 = 'Computer'
item2_price = 579.99
item3 = 'Moinitor'
item3_price = 124.89
total = "Total"
total_sum = item1_price+item2_price+item3_price
message = "Thanks for shopping with us today!"

store_info = '{}\n{:^40}\n{:^40}\n{:^40}\n{}'.format(border1, store_name, store_address, store_state,border2)
product_info = '{:^20}{:^20}'.format(product_info, product_price)
items_and_prices = '{:^20}{:^20}\n{:^20}{:^20}\n{:^20}{:^20}'.format(item1, item1_price,item2,item2_price,item3,item3_price)
total_price = '{}\n{:^40}\n{:^40}\n'.format(border1,total,total_sum,message)
entire_list = f'''{store_info}\n{product_info}\n{items_and_prices}
\n{total_price}\n{border2}\n{message}\n{border1}'''
print (entire_list)