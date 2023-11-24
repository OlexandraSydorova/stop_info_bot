import telebot

bot = telebot.TeleBot('5930476206:AAET7tDk2amG4AL75hfaglpCcsWzDrxFDAQ')
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    sent_msg = bot.send_message(message.chat.id, "Привіт, друже! Напиши свій відгук пройденого курсу.")
    bot.register_next_step_handler(sent_msg, thanks)


@bot.message_handler(func=lambda msg: True)
def thanks(message):
    sign = message.text
    f = open('db.txt', 'a')
    f.write(message.text+'\n')
    print(sign)
    sent_msg = bot.send_message(
        message.chat.id, "Дякую за те, що поділилися своїм досвідом! Ви можете доповнити свою історію, або розповісти нову, написавши нам повідомлення.")

bot.infinity_polling()
