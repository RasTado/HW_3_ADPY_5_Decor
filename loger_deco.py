from datetime import datetime
import os


# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась и возвращаемое значение.
def loger(function):

    def some_function(*args, **kwargs):

        result = function(*args, **kwargs)
        key_log = f'Function:  {function.__name__}   ' \
                  f'\nTime:   {datetime.now()}  ' \
                  f'\nArguments:  {args} {kwargs}  ' \
                  f'\nResult:  {[r for r in result]}  ' \
                  f'\n_______________________'

        with open('log.txt', 'a') as file_obj:
            file_obj.write(key_log)
        print('\nLogged...')
        return result

    return some_function


# 2. Написать декоратор из п.1, но с параметром – путь к логам.
def path_loger(path_l):

    def loger_2(function):

        def some_function(*args, **kwargs):

            result = function(*args, **kwargs)
            key_log = f'Function:  {function.__name__}   ' \
                      f'\nTime:   {datetime.now()}  ' \
                      f'\nArguments:  {args} {kwargs}  ' \
                      f'\nResult:  {[r for r in result]}  ' \
                      f'\n_______________________\n'
            os.makedirs(path_l, exist_ok=True)
            full_path_r_files = os.path.join(os.getcwd(), path_l, f'{function.__name__}.txt')
            with open(full_path_r_files, 'a') as file_obj:
                file_obj.write(key_log)
            print(f'Logged in {full_path_r_files}')
            return result

        return some_function

    return loger_2


# 3. Применить написанный логгер к приложению из любого предыдущего д/з.
# In HW34itergeneratorwithloger.py