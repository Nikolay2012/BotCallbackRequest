'''
    Модуль який надсилає повідомлення від бота до користувача
'''

import modules.create_bot as m_bot
import modules.search_path_to_file as m_path_to_file
import modules.create_inline_keyboard as m_inline_keyboard

text = "NEW\nMacBook Pro 16\n164 000 грн"
def send_message_user(message):
    if message.text.lower() == "get picture":
        path_file = m_path_to_file.search_path_to_file('images/1.jpeg')
        m_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            text,
            reply_markup= m_inline_keyboard.inline_keyboard
        )

    m_bot.bot.register_next_step_handler(message, send_message_user)
