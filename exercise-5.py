import os
import telebot
import speech_recognition as sr
import subprocess

TOKEN = '2144322902:AAGNT2mbleldzYL53vQ3adDtriLLHTxnvnA'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f'{message.chat.id}.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)

    process = subprocess.Popen(['d:/ffmpeg.exe', '-i', f'{message.chat.id}.ogg', f'{message.chat.id}.wav'])
    process.wait()

    r = sr.Recognizer()
    with sr.WavFile(f'{message.chat.id}.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio,language='ru-RU')

    print(text)
    bot.send_message(message.from_user.id, text)

    os.remove(f'{message.chat.id}.wav')

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)





