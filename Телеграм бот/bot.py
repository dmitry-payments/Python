import telebot

TOKEN = 
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    print("Бот начал работу")
    bot.send_message(message.chat.id, "Бот активирован и готов к работе")


@bot.message_handler(content_types=['text'])
def send_text(message):
    print("Получено новое сообщение:", message.text)
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Приветствую, хозяин")
    elif message.text == "Пока":
        bot.send_message(message.chat.id, "Уже уходишь? Я буду скучать -(")
    else:
        bot.send_message(message.chat.id, "Я еще слишком глуп, и не знаю что ответить...")


bot.polling()
