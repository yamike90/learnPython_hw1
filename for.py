"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

grades = [{'school_class': '4а', 'scores': [3,4,4,5,2]},
            {'school_class': '3б', 'scores': [5,4,3,5,2]},
            {'school_class': '5в', 'scores': [3,4,4,5,2]},
            {'school_class': '2а', 'scores': [3,5,4]},
            {'school_class': '7б', 'scores': [5,4,1,5,2]},
            {'school_class': '3а', 'scores': [5,5,5,5]},
            {'school_class': '4в', 'scores': [1,2,4,2,2,5,5]}
    ]

def main(grades):
    a = 0
    for i in grades:
        a += (sum(i['scores']) / len(i['scores']))
    print("Средний балл по школе равен: {}.".format(a / len(grades)))

    for i in grades:
        #print ("Средний балл класса " + i['school_class'] + ": " + str(sum(i['scores']) / len(i['scores'])))
        print("Средний балл класса {} равен: {}.".format(i['school_class'], sum(i['scores']) / len(i['scores'])))
        
main(grades)
