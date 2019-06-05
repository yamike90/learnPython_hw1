"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def greet_user(bot, update):
    text = '''Привет!
Используй /planet, чтобы найти в каком созведии сейчас находится планета.

Например, /planet Mars

Список планет:
Sun
Moon
Mercury
Venus
Mars
Jupiter
Saturn
Uranus
Neptune
Pluto
'''
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    update.message.reply_text(f'И тебе {user_text}. Используй /planet, чтобы найти в каком созведии сейчас находится планета.')

def planet_constellation(bot, update):
    try:
        current_date = update.message.date
        planet = update.message.text.split()[1].lower().capitalize()

        try:
            planet_object = getattr(ephem, planet)(current_date)
            const = ephem.constellation(planet_object)
            text = f'Планета "{planet}" находится сейчас в созвездии {const}.'
        except AttributeError:
            text = "Нет такой планеты!"
     
    except IndexError:
        text = "Напиши название планеты после /planet!"

    update.message.reply_text(text)

def next_full_moon(bot, update):
    try:
        date = update.message.text.split()[1]
    except IndexError:
        date = update.message.date

    next_full_moon_date  = ephem.next_full_moon(date)
    text = f'Ближайшее полнолуние будет {next_full_moon_date}.'

    update.message.reply_text(text)

def cities(bot, update):

    cities = ['Москва', 'Астана', 'Абакан']
    #доделать https://learn.python.ru/lessons/tasks_lesson2.html?full#6
 
def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    
    mybot.start_polling()
    mybot.idle()
  
if __name__ == "__main__":
    main()
