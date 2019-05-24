"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def avg_grade(grades):
    a = 0
    b = 0
    for grade in grades:
        a += sum(grade['scores'])
        b += len(grade['scores'])
        print("Средний балл класса {} равен: {}.".format(grade['school_class'], sum(grade['scores']) / len(grade['scores'])))
    print("Средний балл по школе равен: {}.".format(a / b))

def main():

    grades1 = [{'school_class': '4а', 'scores': [3,4,4,5,2]},
                {'school_class': '3б', 'scores': [5,4,3,5,2]},
                {'school_class': '5в', 'scores': [3,4,4,5,2]},
                {'school_class': '2а', 'scores': [3,5,4]},
                {'school_class': '7б', 'scores': [5,4,1,5,2]},
                {'school_class': '3а', 'scores': [5,5,5,5]},
                {'school_class': '4в', 'scores': [1,2,4,2,2,5,5]}
        ]

    grades = [
    {'school_class': '4а', 'scores': [3]},
    {'school_class': '4в', 'scores': [5,5,5,5,5,5,5,5,5,5,5,5,5,5]},
]

    avg_grade(grades)

if __name__ == "__main__":
    main()
