'''
    Модуль який перевіряє та обробляє команду старт
'''
import modules.create_bot as m_bot
import modules.create_keyboard_get_picture as m_keyboard_picture
import modules.send_message_user as m_send_message_user

@m_bot.bot.message_handler(commands=["start"])

def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id,
        "Hi, user",
        reply_markup= m_keyboard_picture.keyboard
    )
    m_bot.bot.register_next_step_handler(
        message, 
        m_send_message_user.send_message_user
    )