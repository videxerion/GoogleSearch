from gs_modules.logo import print_logo
from gs_modules.docmunets import *
from gs_modules.extensions import get_extensions
from gs_modules.url import get_url

import os

documents = document_module()


site = get_url()
extensions = get_extensions()

os.system('clear')
print_logo()

array = documents.search_documents_site(site, extensions=extensions)

documents.get_files(array)

print('\n\n[-] --------------------------------- ФАЙЛЫ --------------------------------- [-]')
for i in range(len(array)):
    print(f'[+] {array[i]}')
print('[-] ------------------------------------------------------------------------- [-]')


#  Copyright (c) 2021 videxerion
