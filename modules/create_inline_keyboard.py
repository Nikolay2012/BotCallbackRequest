'''

'''
import telebot
import modules.create_inline_button as m_inline_bt

inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(m_inline_bt.inline_button1, m_inline_bt.inline_button2)
