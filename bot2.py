import telebot


TOKEN = '7518700109:AAE7qY6M7Mg52f_ewR1H8GCKO2FoRKYzusI'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('songs')
    button2 = telebot.types.KeyboardButton('my love songs')
    button3 = telebot.types.KeyboardButton('folk songs')
    button4 = telebot.types.KeyboardButton('jazz songs')
    button5 = telebot.types.KeyboardButton('Help')
    button6 = telebot.types.KeyboardButton('english songs')
    keyboard.add(button1, button2, button3, button4, button5, button6)

    bot.send_message(message.chat.id, "Welcome to my shopping bot! Please choose an option:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'songs')
def send_photo(message):
    with open('telebot.py/a-logo-for-a-music-company-that-is-made-by-song-brand-vector.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="This is the first photo. Nice!")

@bot.message_handler(func=lambda message: message.text == ' my love songs')
def send_audio(message):
    with open('telebot.py/Djo - End of Beginning.mp3', 'rb') as img:
        bot.send_audio(message.chat.id, img, caption="This is the first photo. Nice!")

@bot.message_handler(func=lambda message: message.text == 'folk songs')
def send_audio(message):
   
    with open('telebot.py/Disturbed - The Sound Of Silence (CYRIL Remix).mp3', 'rb') as img:
        bot.send_audio(message.chat.id, img, caption="Это аудиосообщение.")        


@bot.message_handler(func=lambda message: message.text == 'jazz songs')
def send_jazz(message):
    
    with open('telebot.py/David A. Stewart - Lily Was Here (feat. Candy Dulfer).mp3', 'rb') as vid:
        bot.send_audio(message.chat.id, vid, caption="Это аудиосообщение.")
   

@bot.message_handler(func=lambda message: message.text == 'Help')
def send_help(message):
    bot.send_message(message.chat.id, "Это справочное сообщение. Введите /start для начала работы с ботом.")


@bot.message_handler(func=lambda message: message.text == 'english songs ')
def send_audio(message):
   
  
    with open('telebot.py/Lana_Del_Rey_-_Diet_Mountain_Dew_(www.muzofan.net).mp3', 'rb') as img:
        bot.send_audio(message.chat.id, img, caption="Это аудиосообщение.")


bot.polling()