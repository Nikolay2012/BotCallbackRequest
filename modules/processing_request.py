import modules.create_bot as m_bot

@m_bot.bot.callback_query_handler(func= lambda callback: callback.data)

def processing_callback(callback):
    if callback.data == "замовити":
        m_bot.bot.send_message(
            callback.message.chat.id,
            "Замовлення прийнято!\nОчікуйте зворотнього зв'язку!",
        )