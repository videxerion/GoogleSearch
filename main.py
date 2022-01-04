from gs_modules.logo import print_logo
from gs_modules.docmunets import *
from gs_modules.extensions import get_extensions
from gs_modules.argvParse import parse_argv
from gs_modules.metadata import metadata_module
from gs_modules.checks import integrity_check, check_to_empty_folder
from colorama import init
from colorama import Fore
import os
import sys

flags, arguments = parse_argv(sys.argv)
flags_names = list(flags.keys())

if flags == {} or len(arguments) == 0 or '--help' in flags_names:
    print('python main.py {url} {flags}\n\t--documents or -doc -- поиск документов в гугле связанных с сайтом\n\t--download or -down -- скачать найденные документы\n\t--metadata or -meta -- достать мета данные полученных файлов')
    exit(0)


init(autoreset=True)

if not integrity_check():
    exit(-1)

if not check_to_empty_folder('search_files'):
    clear_choise = input(Fore.LIGHTRED_EX + 'Внимание!\nДиректория с файлами не пуста, удалить содержимое? [Y/N]\n')
    if clear_choise.lower() in ['yes', 'y', 'ye']:
        file_list = os.listdir('search_files')
        for i in range(len(file_list)):
            os.remove(f'search_files/{file_list[i]}')

documents = document_module()
metadata = metadata_module()

site = arguments[0]
extensions = get_extensions()

os.system('clear')
print_logo()

if '--documents' in flags_names or '-doc' in flags_names:
    array = documents.search_documents_site(site, extensions=extensions)
    if '--download' in flags_names or '-down' in flags_names:
        documents.get_files(array)
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

#  Copyright (c) 2021 videxerion
