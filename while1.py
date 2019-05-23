"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        user_state  = input('Как дела? ')
        if user_state == 'Хорошо':
            print('Хорошо, что хорошо')
            break
        else:
            print('А я думал, что хорошо')

ask_user()
