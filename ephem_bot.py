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

        if planet == "Sun":
            planet_object = ephem.Sun(current_date)
        elif planet == "Moon":
            planet_object = ephem.Moon(current_date)
        elif planet == "Mercury":
            planet_object = ephem.Mercury(current_date)
        elif planet == "Venus":
            planet_object = ephem.Venus(current_date)
        elif planet == "Mars":
            planet_object = ephem.Mars(current_date)
        elif planet == "Jupiter":
            planet_object = ephem.Jupiter(current_date)
        elif planet == "Saturn":
            planet_object = ephem.Saturn(current_date)
        elif planet == "Uranus":
            planet_object = ephem.Uranus(current_date)
        elif planet == "Neptune":
            planet_object = ephem.Neptune(current_date)
        elif planet == "Pluto":
            planet_object = ephem.Pluto(current_date)
        else:
            update.message.reply_text("Нет такой планеты!")

        const = ephem.constellation(planet_object)
        text = f'Планета "{planet}" находится сейчас в созвездии {const}.'
        update.message.reply_text(text)

    except IndexError:
        update.message.reply_text("Напиши название планеты после /planet!")
 
def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    
    mybot.start_polling()
    mybot.idle()
  
if __name__ == "__main__":
    main()
