import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import unquote

class google_module():
    def __init__(self):
        self.session = requests.session()
        self.headres = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru,ru-MD;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36'
        }

    def search(self, request):
        g = 0
        return_array = []
        while True:
            time.sleep(1)
            html = self.session.get(f'https://www.google.com/search?q={request}&start={g}0')
            soup = BeautifulSoup(html.text, 'html.parser')
            links_not_clean = soup.find_all('div', {'class': 'kCrYT'})
            links_clean = []
            for i in range(len(links_not_clean)):
                string = str(links_not_clean[i])
                if string.find('href') != -1:
                    links_clean.append(unquote(unquote(string[string.find('/url?q=') + 7: string.find('&amp')])))
                    # print(string[string.find('/url?q=') + 7: string.find('&amp')])
            if links_clean == []:
                return return_array
            else:
                for i in range(len(links_clean)):
                    return_array.append(links_clean[i])
            g += 1

#  Copyright (c) 2021 videxerion
