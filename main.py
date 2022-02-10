#  Copyright (c) 2021-2022 videxerion
#  Source code: https://github.com/videxerion/GoogleSearch


from gs_modules.logo import print_logo
from gs_modules.docmunets import *
from gs_modules.extensions import get_extensions
from gs_modules.argvParse import parse_argv
from gs_modules.metadata import metadata_module
from gs_modules.checks import check_to_avalible_directory, check_to_empty_folder
from colorama import init
from colorama import Fore
import os
import sys

os.system('clear')
print_logo()

flags, arguments = parse_argv(sys.argv)
flags_names = list(flags.keys())
path = flags['-down'] if '-down' in flags else flags['--download']

if flags == {} or len(arguments) == 0 or '--help' in flags_names:
    print('python main.py {url} {flags}',
          '\n\t--documents or -doc -- поиск документов в гугле связанных с сайтом',
          '\n\t--download or -down {path to folder} -- скачать найденные документы в указанную директорию',
          '\n\t--metadata or -meta -- достать мета данные полученных файлов')
    exit(0)


init(autoreset=True)

try:
    arguments.remove('main.py')
except:
    pass

if check_to_avalible_directory(path):
    if not check_to_empty_folder(path):
        clear_choise = input(Fore.LIGHTRED_EX + 'Внимание!\nДиректория с файлами не пуста, удалить содержимое? [Y/N]\n')
        if clear_choise.lower() in ['yes', 'y', 'ye']:
            file_list = os.listdir(f'{path}')
            for i in range(len(file_list)):
                os.remove(f'{path}/{file_list[i]}')
else:
    exit(-1)


documents = document_module()
metadata = metadata_module()

site = arguments[0]
extensions = get_extensions()

if '--documents' in flags_names or '-doc' in flags_names:
    array = documents.search_documents_site(site, extensions=extensions)
    if '--download' in flags_names or '-down' in flags_names:
        documents.get_files(array, path)
if '--metadata' in flags_names or '-meta' in flags_names:
    meta = metadata.get_meta_data()


os.system('clear')
print_logo()


if '--documents' in flags_names or '-doc' in flags_names:
    print('\n\n[-] --------------------------------- ФАЙЛЫ --------------------------------- [-]')
    for i in range(len(array)):
        print(Fore.LIGHTGREEN_EX + f'[+] {array[i]}')
    print('[-] ------------------------------------------------------------------------- [-]')

if '--metadata' in flags_names or '-meta' in flags_names:
    print('\n\n[-] ------------------------------ МЕТА ДАННЫЕ ------------------------------ [-]')
    for i in range(len(meta)):
        print(Fore.LIGHTRED_EX + '[-]')
        array_meta = meta[i]
        file_name = array_meta[0]
        meta_dict = array_meta[1]
        meta_keys = list(meta_dict.keys())
        print(Fore.LIGHTGREEN_EX + f'[+] {file_name}')
        for g in range(len(meta_keys)):
            print(Fore.LIGHTYELLOW_EX + f'[#] {meta_keys[g]}: {meta_dict[meta_keys[g]]}')
    print('[-] ------------------------------------------------------------------------- [-]')


