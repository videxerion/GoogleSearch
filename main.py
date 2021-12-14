from gs_modules.logo import print_logo
from gs_modules.docmunets import *
from gs_modules.extensions import get_extensions
from gs_modules.url import get_url
from gs_modules.metadata import metadata_module
import os

documents = document_module()
metadata = metadata_module()

site = get_url()
extensions = get_extensions()

os.system('clear')
print_logo()

array = documents.search_documents_site(site, extensions=extensions)

documents.get_files(array)

meta = metadata.get_meta_data()

print('\n\n[-] --------------------------------- ФАЙЛЫ --------------------------------- [-]')
for i in range(len(array)):
    print(f'[+] {array[i]}')
print('[-] ------------------------------------------------------------------------- [-]')

print('\n\n[-] ------------------------------ МЕТА ДАННЫЕ ------------------------------ [-]')
for i in range(len(meta)):
    print('[-]')
    array_meta = meta[i]
    file_name = array_meta[0]
    meta_dict = array_meta[1]
    meta_keys = list(meta_dict.keys())
    print(f'[+] {file_name}')
    for g in range(len(meta_keys)):
        print(f'[#] {meta_keys[g]}: {meta_dict[meta_keys[g]]}')
print('[-] ------------------------------------------------------------------------- [-]')

#  Copyright (c) 2021 videxerion
