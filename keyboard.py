import telebot
import sqlite3
import sql 

db_comics = sql.sqll_comics('comics.db')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Комиксы')
keyboard1.row('Мультфильмы', "Сериалы", "Фильмы")

keyboard_comics = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_comics.row('Тор')
keyboard_comics.row('Человек-паук')
keyboard_comics.row('Халк')

keybord_pauk = telebot.types.ReplyKeyboardMarkup(True, True)
keybord_pauk.row('Amazing')
keybord_pauk.row('Marvel Knights')
keybord_pauk.row('Spectacular')

def generate_key(name, col):
    keyboard_temp = telebot.types.ReplyKeyboardMarkup(True, True)
    for i in range(0, col):
        st = f'{name} #{i}'
        if db_comics.comics_in_base(st):
            keyboard_temp.row(st)
    return keyboard_temp

keyboard_amazing = generate_key('Amazing Spider-Man', 450)