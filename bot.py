from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

PLANETS = ['Mars', 'Venus', 'Saturn', 'Pluto', 'Mercury', 'Uranus', 'Jupiter']

import ephem
import datetime

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    bot_functions = 'Функции бота:'
    about = '/planet - узнать созвездие планеты'
    print(text)
    print(bot_functions)
    print(about)
    update.message.reply_text(text)
    update.message.reply_text(bot_functions)
    update.message.reply_text(about)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def select_planet(bot, update):
    text = 'Выбери планету:\n/Mars\n/Venus\n/Saturn\n/Pluto\n/Mercury\n/Uranus\n/Jupiter'
    print(text)
    update.message.reply_text(text)

'''def planet_info(bot, update):
    user_planet = update.message.text.strip('/')
    print(user_planet)
    list_planet = ['Mars', 'Venus', 'Saturn', 'Pluto', 'Mercury', 'Uranus', 'Jupiter']
    realtime_date = datetime.datetime.now().strftime("%Y/%m/%d")
    if user_planet.lower().capitalize() in list_planet:
        planet = getattr(ephem, user_planet[1].lower().capitalize())
        planet = planet(realtime_date)
        const = ephem.constellation(planet)
        res = f'Планета {user_planet[1].lower().capitalize()} {realtime_date} находится в созвездии {const[1]}'
        print(res)
        update.message.reply_text(res)
    else:
        res = 'Ошибка! Попробуйте ввести название Mars, Earth, Venus, Saturn, Pluto, Mercury, Uranus, Jupiter'
        print(res)
        update.message.reply_text(res)'''
def planet_info(bot, update):
    user_planet = update.message.text.strip('/')
    #list_planet = ['Mars', 'Venus', 'Saturn', 'Pluto', 'Mercury', 'Uranus', 'Jupiter']
    realtime_date = datetime.datetime.now().strftime("%Y/%m/%d")

    planet = getattr(ephem, user_planet)
    planet = planet(realtime_date)
    const = ephem.constellation(planet)
    res = f'Планета {user_planet} {realtime_date} находится в созвездии {const[1]}'
    print(res)
    update.message.reply_text(res)
    #else:
        #res = 'Ошибка! Попробуйте ввести название Mars, Earth, Venus, Saturn, Pluto, Mercury, Uranus, Jupiter'
        #print(res)
        #update.message.reply_text(res)

def main():
    mybot = Updater('886652216:AAEs_2UulyBgeNc_YgwbjpLf4BI0PIIN00Y', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', select_planet))
    dp.add_handler(CommandHandler(PLANETS, planet_info))
   
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()