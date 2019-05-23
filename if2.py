"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):

    if type(str1) != str or type(str2) != str:
        result = 0
    elif str1 == str2:
        result = 1
    elif str1 >= str2:        
        result = 2
    elif str1 != str2 and str2 == "learn":
        result = 3
    else:
        result = "Не предусмотрено заданием"

    print(result)

str_list = [[1, "abc"],
            ["abc", 1],
            [1, 1],
            ["abc", "abc"],
            ["abcd", "abc"],
            ["abc", "learn"],
            ["abc", "learnlearn"]
            ]

for i in str_list:
    main(i[0], i[1])

#str1 = 1
#str2 = "abc"
#main(str1, str2) # 0

#str1 = "abc"
#str2 = 1
#main(str1, str2) # 0

#str1 = 1
#str2 = 1
#main(str1, str2) # 0

#str1 = "abc"
#str2 = "abc"
#main(str1, str2) # 1

#str1 = "abcd"
#str2 = "abc"
#main(str1, str2) # 2

#str1 = "abc"
#str2 = "learn"
#main(str1, str2) # 3

#str1 = "abc"
#str2 = "learnlearn"
#main(str1, str2) # "Не предусмотрено заданием"
