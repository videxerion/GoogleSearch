import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import unquote


class GoogleBan(Exception):
    def __init__(self):
        self.txt = 'Ban in google'


class google_module():
    def __init__(self):
        self.session = requests.session()
        self.headres = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*', 'Connection': 'keep-alive'
        }
        self.session.headers = self.headres

    def search(self, request):
        g = 0
        return_array = []
        while True:
            #time.sleep(0.5)
            html = self.session.get(f'https://www.google.com/search?q={request}&start={g}0', headers=self.headres)
            if html.status_code == 429:
                raise GoogleBan
            soup = BeautifulSoup(html.text, 'html.parser')
            links_not_clean = soup.find_all('div', {'class': 'yuRUbf'})
            links_clean = []
            for i in range(len(links_not_clean)):
                string = str(links_not_clean[i])
                if string.find('href') != -1:
                    links_clean.append(unquote(unquote(string[string.find('" href="') + 8: string.find('" ping="')])))
            if links_clean == []:
                return return_array
            else:
                for i in range(len(links_clean)):
                    return_array.append(links_clean[i])
            g += 1
#  Copyright (c) 2021 videxerion
