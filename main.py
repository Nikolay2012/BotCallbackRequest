'''
    Модуль який запускає в роботу весь проект 
'''
import modules.create_bot as m_bot
import modules.command_start as m_start
import modules.processing_request

m_bot.bot.polling(none_stop = True)