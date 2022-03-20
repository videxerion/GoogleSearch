from colorama import init
from colorama import Fore
import os
import requests

init(autoreset=True)


def check_to_avalible_directory(path):
    try:
        file = open(f'{path}/testfile', 'w')
        file.close()
        os.remove(f'{path}/testfile')
        return True
    except Exception as err:
        print(Fore.RED + f'[-] {err}')
        return False


def check_extensions(extensions):
    if len(extensions) == 0:
        return False
    else:
        return extensions.split(',')


def check_to_empty_folder(name_folder):
    files = os.listdir(name_folder)
    if not files:
        return True
    else:
        return False


def check_to_exist_url(url):
    try:
        if url.find('http') == -1 and url.find('https') == -1:
            response = requests.get(f'http://{url}')
        else:
            response = requests.get(f'{url}')
        return True
    except Exception as ex:
        print(Fore.RED + '[-] ' + f'Невозможно связаться с сайтом {url}')
        print(Fore.RED + f'[-] {ex}')
        return False
