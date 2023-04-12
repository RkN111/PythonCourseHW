# Задача 5. Да се принтира списък със всички функции от модула “re”, които съдържат
# думата “find”.



import re
a = dir(re)
list2 = [i for i in a if re.search('find', i)]
print(list2)