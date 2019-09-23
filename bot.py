from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

PLANETS = ['Mars', 'Venus', 'Saturn', 'Pluto', 'Mercury', 'Uranus', 'Jupiter']
CITIES = ['Москва','Альметьевск', 'Уфа', 'Хабаровск', 'Томск', 'Екатеринбург', 'Оренбург', 'Кемерово', 'Грозный', 'Воскресенск', 'Рязань', 'Новосибирск', 'Калуга', 'Брянск', 'Кострома', 'Алушта', 'Орел', 'Киров', 'Владимир', 'Ряжск', 'Курск', 'Коломна', 'Абакан', 'Тула', 'Нью-Йорк', 'Вашингтон']

import ephem
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')

from datetime import date, timedelta, datetime

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Добро пожаловать, это тестовый информационный бот.'
    bot_functions = 'Функции бота:'
    about = '/planet - узнать созвездие планеты'
    about_1 = 'введите /wordcount + слова - посчитает количество слов'
    about_2 = 'введите /next_full_moon + дата (год-месяц-день) - узнать когда ближайшее полнолуние'
    print(text)
    print(bot_functions)
    print(about)
    print(about_1)
    print(about_2)
    update.message.reply_text(text)
    update.message.reply_text(bot_functions)
    update.message.reply_text(about)
    update.message.reply_text(about_1)
    update.message.reply_text(about_2)

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

def word_count(bot, update):
    user_words = update.message.text.strip('/wordcount')
    if user_words != '':
        user_words_list = user_words.split()
        res = f'Количество слов в строке: {len(user_words_list)}'
        print(res)
        update.message.reply_text(res)
    else:
        text = 'Слова не введены'
        print(text)
        update.message.reply_text(text)

def next_full_moon(bot, update):
    user_text = update.message.text.strip('/next_full_moon ')
    full_moon = ephem.next_full_moon(user_text)
    res_dt = datetime.strptime(str(full_moon), '%Y/%m/%d %H:%M:%S')
    res = res_dt.strftime('%A %d %B %Y %H:%M:%S')
    answ = f'Следующее полнолуние будет: {res}'
    print(answ)
    update.message.reply_text(answ)

'''def cities(bot, update):
    game_city = CITIES
    deleted_cities = []
    user_city = update.message.text.strip('/cities ')
    user_city = user_city.lower().capitalize()
    if user_city in game_city:
        for bot_city in 
        user_city[-1].upper()'''





    

def main():
    mybot = Updater('886652216:AAEs_2UulyBgeNc_YgwbjpLf4BI0PIIN00Y', request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', select_planet))
    dp.add_handler(CommandHandler(PLANETS, planet_info))
    dp.add_handler(CommandHandler('wordcount', word_count))
    dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
    #dp.add_handler(CommandHandler('cities', cities))

   
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()