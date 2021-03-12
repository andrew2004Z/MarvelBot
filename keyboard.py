import telebot

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
