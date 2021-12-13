from gs_modules.logo import print_logo
from gs_modules.docmunets import *
from gs_modules.extensions import get_extensions
import os

documents = document_module()

site = 'co44tula.ru'
extensions = get_extensions()

os.system('clear')
print_logo()

print('[-] --------------------------------- ФАЙЛЫ --------------------------------- [-]')
array = documents.search_documents_site(site, extensions=extensions)
for i in range(len(array)):
    print(f'[+] {array[i]}')
print('[-] ------------------------------------------------------------------------- [-]')

#  Copyright (c) 2021 videxerion
