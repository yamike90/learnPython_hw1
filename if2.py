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

def compare(str1, str2):

    #if type(str1) != str or type(str2) != str:
    if isinstance(str1, str) == False or isinstance(str2, str) == False:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):        
        return 2
    elif str2 == "learn":
        return 3
    else:
        return "Не предусмотрено заданием"

def main():
    str_list = [[1, "abc"],
                ["abc", 1],
                [1, 1],
                ["abc", "abc"],
                ["abcd", "abc"],
                ["abc", "learn"],
                ["abc", "learnlearn"]
                ]

    for i in str_list:
        print(compare(i[0], i[1]))

    #for str1, str2 in str_list:
        #print(compare_strings(str1, str2))

    #for i in str_list:
        #str1, str2 = i
        #print(compare_strings(str1, str2))

    #foo = [1,2]
    #foo1, foo2 = foo
    #print(foo1, foo2)
    #print(*foo)

if __name__ == "__main__":
    main()

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
