import telebot
import keyboard
bot = telebot.TeleBot('1417817254:AAGRJdZkQSsNgWZO7Sfp8REFD1aepTPSGJg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, в этом боте ты сможешь почитать комиксы Marvel и посмотреть фильмы и сериалы из киновселенной Marvel', reply_markup=keyboard.keyboard1)


@bot.message_handler(content_types=['text'])
def comics_video(message):
    if message.text == 'Комиксы':
        bot.send_message(message.chat.id, 'Тут ты сможешь найти множество комиксов Marvel', reply_markup=keyboard.keyboard_comics)
    elif message.text == 'В начало':
        bot.send_message(message.chat.id, 'Вы вернулись в начало', reply_markup=keyboard.keyboard1)
    elif message.text == 'Человек-паук':
        bot.send_message(message.chat.id, 'Здесь есть множество комиксов про Человека-паука', reply_markup=keyboard.keybord_pauk)
    elif message.text == 'Amazing Spider-Man #1':
        bot.send_document(message.chat.id, 'BQACAgIAAxkDAAILlmBKXEkZNZMXjpL89VK7e-HitKVHAAJbDQACpElQSlrX9e3ve4LbHgQ')

bot.polling()
