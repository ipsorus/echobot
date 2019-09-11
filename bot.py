from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import ephem

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def select_planet(bot, update):
    text = 'Выбери планету:\n/Mars\n/Earth\n/Venus\n/Saturn\n/Pluto\n/Mercury\n/Uranus\n/Jupiter'
    
    print(text)
    update.message.reply_text(text)

def planet_info_Mars(bot, update):
    res = ephem.Mars('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Earth(bot, update):
    res = ephem.Earth('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Jupiter(bot, update):
    res = ephem.Jupiter('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Venus(bot, update):
    res = ephem.Venus('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Uranus(bot, update):
    res = ephem.Uranus('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Pluto(bot, update):
    res = ephem.Pluto('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Neptune(bot, update):
    res = ephem.Neptune('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Saturn(bot, update):
    res = ephem.Saturn('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])

def planet_info_Mercury(bot, update):
    res = ephem.Mercury('2019/09/12')
    const = ephem.constellation(res)
    update.message.reply_text(const[1])


def main():
    mybot = Updater('886652216:AAEs_2UulyBgeNc_YgwbjpLf4BI0PIIN00Y', request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', select_planet))
    dp.add_handler(CommandHandler('Mars', planet_info_Mars))
    dp.add_handler(CommandHandler('Earth', planet_info_Earth))
    dp.add_handler(CommandHandler('Mercury', planet_info_Mercury))
    dp.add_handler(CommandHandler('Jupiter', planet_info_Jupiter))
    dp.add_handler(CommandHandler('Venus', planet_info_Venus))
    dp.add_handler(CommandHandler('Saturn', planet_info_Saturn))
    dp.add_handler(CommandHandler('Neptune', planet_info_Neptune))
    dp.add_handler(CommandHandler('Uranus', planet_info_Uranus))
    dp.add_handler(CommandHandler('Pluto', planet_info_Pluto))

    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()