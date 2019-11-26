import telebot
import apiai
import json


bot = telebot.TeleBot("1051308879:AAESC8UYi9Q9SI6QIJuXhq-nlz9dYWoRe1c")


@bot.message_handler(commands=['start'])
def start_message(message):
    request = apiai.ApiAI('40eb1f5c8af449fead6756313620120f').text_request() # токен DialogFlow 
    request.lang = 'ru' 
    request.session_id = 'session_1' # сюда можно писать что захотите 
    request.query = message.text 
    response = json.loads(request.getresponse().read().decode('utf-8')) 
    answer = str(response['result']['fulfillment']['speech']) 
    if answer != '': 
       bot.send_message(message.chat.id, answer) 
       bot.register_next_step_handler(message, send_message23) 
    elif message.text == 'Назад': 
       bot.send_message(message.chat.id, 'Хорошо\nВыбирите что хотите?', reply_markup=main_markup(message) 
       ) 
       bot.register_next_step_handler(message, start_message) 
    else: 
       bot.send_message(message.chat.id, 'Прости, но я тебя не понимаю😓\n' 
   'Напиши /start или /help и я тебе обязательно постораюсь помощь)')

bot.polling()
