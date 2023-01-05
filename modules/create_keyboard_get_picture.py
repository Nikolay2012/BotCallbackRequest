'''
    Модуль для створення клавіатури,яка відпрвляє повідомлення
'''
import telebot
import modules.create_button_get_picture as m_bt_get_picture

keyboard = telebot.types.ReplyKeyboardMarkup()

keyboard.add(m_bt_get_picture.button_picture)

