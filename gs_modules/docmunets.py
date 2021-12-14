from gs_modules.google import *

google = google_module()


class document_module():
    def search_documents_site(self, site, extensions):
        return_arr = []

        for i in range(len(extensions)):
            arr = google.search(f'site:{site} filetype:{extensions[i]}')
            for g in range(len(arr)):
                return_arr.append(arr[g])
            print(f'[#] search {extensions[i]} done...')
        return return_arr

#  Copyright (c) 2021 videxerion
