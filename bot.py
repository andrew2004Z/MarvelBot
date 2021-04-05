import telebot
import keyboard
import sqlite3
from sql import sqll_user, sqll_comics
import datetime
from image_to_pdf import colpage_pdf, get_path_json, read_json
import time

def get_id(message, db_comics, path1, path2):
    for i in range(0, 1000):
        try:
            name = f'{path2}{i}'
            if db_comics.comics_in_base(name):
                pass
            else:
                #f = open(f'{path1}\{name}\{name}.pdf', 'rb')
                #f1 = open(f'{path1}\{name}\\001.jpg', 'rb')
                cover = bot.send_photo(message.chat.id, open(f'{path1}\{name}\\001.jpg', 'rb'))
                msg = bot.send_document(message.chat.id, open(f'{path1}\{name}\{name}.pdf', 'rb'))
                comics_id = msg.document.file_id
                cover_id = cover.photo[0].file_id
                print(cover_id)
                db_comics.add_comics(name, comics_id, cover_id, colpage_pdf(f'{path1}\{name}\{name}.pdf'))
                time.sleep(1)
        except:
            pass

bot = telebot.TeleBot('1417817254:AAGRJdZkQSsNgWZO7Sfp8REFD1aepTPSGJg')

db_user = sqll_user('users.db')
db_comics = sqll_comics('comics.db')
@bot.message_handler(commands=['start'])
def start_message(message):
    if not db_user.user_in_base(message.chat.id):
        db_user.add_user(message.chat.id, datetime.datetime.now(), 0)
    bot.send_message(message.chat.id, 'Привет, в этом боте ты сможешь почитать комиксы Marvel и посмотреть фильмы и сериалы из киновселенной Marvel',
                     reply_markup=keyboard.keyboard1)


@bot.message_handler(content_types=['text'])
def comics_video(message):
    global db_comics
    if message.text == 'Комиксы':
        bot.send_message(message.chat.id, 'Тут ты сможешь найти множество комиксов Marvel',
                         reply_markup=keyboard.keyboard_comics)
    elif message.text == 'В начало':
        bot.send_message(message.chat.id, 'Вы вернулись в начало',
                         reply_markup=keyboard.keyboard1)
    elif message.text == 'Человек-паук':
        bot.send_message(message.chat.id, 'Здесь есть множество комиксов про Человека-паука',
                         reply_markup=keyboard.keybord_pauk)
    elif message.text == 'Amazing':
        bot.send_message(message.chat.id, 'Здесь есть множество комиксов из серии Amazing Spider-man, если вы не нашли нужный выпуск попробуйте ввести "Amazing Spider-Man #1" вместо 1 нужный номер (без ковычек)',
                         reply_markup=keyboard.keyboard_amazing)
    elif db_comics.comics_in_base(message.text):
        #print(db_comics.get_cover_id(message.text)[1:])
        bot.send_photo(message.chat.id, db_comics.get_cover_id(message.text)[1:-1], caption=f'{message.text}\nКоличество страниц: {db_comics.get_coll_page(message.text)}')
        #bot.send_photo(message.chat.id, db_comics.get_cover_id(message.text)[1:-1])
        bot.send_document(message.chat.id, db_comics.get_id_pdf(message.text)[1:-1])
    elif message.text == 'Amazing Spider-Man #1':
        bot.send_document(message.chat.id, 'BQACAgIAAxkDAAILlmBKXEkZNZMXjpL89VK7e-HitKVHAAJbDQACpElQSlrX9e3ve4LbHgQ')
    elif message.text == 'test':
        sp1 = get_path_json(read_json('data_json\comics.json'))
        for i in sp1:
            print(i)
            get_id(message, db_comics, i[0].replace(':', " -"), i[1].replace(':', " -"))
            
bot.polling()
#print(get_path_json(read_json('data_json\comics.json')))

