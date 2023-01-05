'''
    Модуль який показує абсолютний шлях до файлу,який вказаний як параметр функції
'''
import os
def search_path_to_file(name_file):
    abs_path = __file__.split('/')
    del abs_path[-1]
    del abs_path[-1]
    abs_path = '/'.join(abs_path)
    abs_path = os.path.join(abs_path, name_file)
    return abs_path

