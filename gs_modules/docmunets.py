from gs_modules.google import *
import requests
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

google = google_module()


class document_module():
    def search_documents_site(self, site, extensions):
        return_arr = []

        for i in range(len(extensions)):
            arr = google.search(f'site:{site} filetype:{extensions[i]}')
            for g in range(len(arr)):
                return_arr.append(arr[g])
            print(Fore.LIGHTYELLOW_EX + f'[#] search {extensions[i]} done...')
        return return_arr

    def get_files(self, linksList):
        for i in range(len(linksList)):
            link = linksList[i]
            name_file = link[link.rfind('/') + 1:]
            file_download = requests.get(link)
            if file_download.status_code == 200:

                print(Fore.LIGHTYELLOW_EX + f'[#] get {name_file} file...')

                file = open(f'search_files/{name_file}', 'wb')
                file.write(file_download.content)
                file.close()

#  Copyright (c) 2021 videxerion
