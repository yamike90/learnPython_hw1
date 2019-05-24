"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

user_dict = {"Как дела?" : "Хорошо!",
        "Что делаешь?" : "Программирую",
        "Чем завтракал?" : "Хлопья и кофе",
        "Что будешь делать летом?" : "Проект на Python",
        }

def ask_user_dict(qa):    
    while True:
        try:
            user_question = input("Задай мне вопрос: ")
            if user_question in qa.keys():
                print(qa[user_question])
            elif user_question == "Пока":
                print("И тебе пока")
                break
            else:
                print('У меня нет ответа на твой вопрос. Попробуй снова')
        except KeyboardInterrupt:
            print('\nПока')
            break

ask_user_dict(user_dict)
