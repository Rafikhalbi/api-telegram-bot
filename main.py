import telebot
from re import search
from requests import get

token = '5490361434:AAEwMGledRVEqWBfiSVECyqBHzuF3-0lyro' # Your Token
bot = telebot.TeleBot(token, parse_mode=None)
@bot.message_handler()
def send_botMessage(message):
    messtxt = message.text.replace('/simi ','')
    get_ = get(f'https://api.simsimi.net/v2/?text={messtxt}&lc=id').text
    messsimi = search(r'{"methods":"GET","success":"(.*?)","noti":"MeoCop#5555"',str(get_))[1]
    bot.reply_to(message, messsimi)

bot.infinity_polling()
