import telebot
 
user_name = ""
memory = ""
state = "Обычный"
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
 
dictinary = {"Привет": "Приветствую",
             "Пока": "Уже уходишь? {}? Я буду скучать -(".format(user_name),
             "Как дела?": "Отлично!",
             "Который час?": "Время действовать!"
 
}
 
@bot.message_handler(commands=['start'])
def start_message(message):
    global user_name
    print("Бот начал работу")
    bot.send_message(message.chat.id, "Бот активирован и готов к работе")
    if not user_name:
        print("Бот отправил запрос на получение имени юзера")
        bot.send_message(message.chat.id, "Приветствую вас, хозяин. Как вы прикажете мне вас называть?")
 
@bot.message_handler(content_types=['text'])
def send_text(message):
    global memory
    global state
    global user_name
    print("Получено новое сообщение:", message.text)
    if state == "Обычный":
        if not user_name:
            user_name = message.text
            print("Бот принял имя юзера")
            bot.send_message(message.chat.id, "Приятно познакомиться, {}".format(user_name))
        else:
            if dictinary.get(message.text) != None:
                bot.send_message(message.chat.id, dictinary[message.text])
            else:
                bot.send_message(message.chat.id, "Нипонятно чёт, хотите что бы я науччился отвечать на это?")
                memory = message.text
                state = "Подтверждение"
    elif state == "Подтверждение":
        if message.text.title() == "Да":
            bot.send_message(message.chat.id, "Отлично, и как же мне отвечать на это?")
            state = "Обучение"
        else:
            bot.send_message(message.chat.id, "Не очень то и хотелось...")
            state = "Обычный"
