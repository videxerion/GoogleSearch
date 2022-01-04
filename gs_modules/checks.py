from colorama import init
from colorama import Fore
import os

init(autoreset=True)


def integrity_check():
    try:
        file = open('search_files/test', 'w')
        file.close()
        os.remove('search_files/test')
    except:
        print(Fore.RED + 'Внимание отсутсвует директория search_files. Попробую её создать...')
        try:
            os.mkdir('search_files')
            print(Fore.GREEN + 'Директория успешно создана!')
        except:
            print(Fore.RED + 'Внимание, не удалось создать директорию\nВозможно не хватает прав')
            return False

    return True


def check_to_empty_folder(name_folder):
    files = os.listdir(name_folder)
    if not files:
        return True
    else:
        return False
