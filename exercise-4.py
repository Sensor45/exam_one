import telebot

TOKEN = '2144322902:AAGNT2mbleldzYL53vQ3adDtriLLHTxnvnA'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def auto_hendler(message):
    text = message.text.lower()
    print(text)
    vowels = 0
    for i in text:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y":
            vowels += 1

    bot.send_message(message.from_user.id, f'Гласных слов в слове: {vowels}')

bot.infinity_polling()

