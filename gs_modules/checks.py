from colorama import init
from colorama import Fore, Back, Style
from gs_modules.url import get_url
import os

init(autoreset=True)


def integrity_check():
    try:
        file = open('url.txt', 'r')
        file.close()
    except:
        print(Fore.RED + '!!!ERROR!!!\nВнимание отсутсвует url.txt. Попробую его создать...')
        try:
            file = open('url.txt', 'w')
            file.close()
            print(Fore.GREEN + 'Файл успешно создан! Просто перезапустите программу')
        except:
            print(Fore.RED + 'Внимание, не удалось создать url.txt!\nВозможно не хватает прав')
        return False

    try:
        file = open('search_files/test', 'w')
        file.close()
        os.remove('search_files/test')
    except:
        print(Fore.RED + '!!!ERROR!!!\nВнимание отсутсвует директория search_files. Попробую её создать...')
        try:
            os.mkdir('search_files')
            print(Fore.GREEN + 'Директория успешно создана! Просто перезапустите программу')
        except:
            print(Fore.RED + 'Внимание, не удалось создать директорию\nВозможно не хватает прав')
        return False
    try:
        get_url()
    except:
        print(Fore.RED + 'Внимание, ошибка при прочтении файла url.txt\nВозможно не хватает прав или файл пуст')
        return False

    return True


def check_to_empty_folder(name_folder):
    files = os.listdir(name_folder)
    if not files:
        return True
    else:
        return False
