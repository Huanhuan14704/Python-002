import requests
from bs4 import BeautifulSoup as bs
import time


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

# 获取页面上所有电影链接后缀列表
urls_suffix = []

for dds in bs_info.find_all('dl', attrs={'class': 'movie-list'}):
    for atag in dds.find_all('a'):
        #print(atag.get('href'))
        urls_suffix.append(atag.get('href'))

# 只取前n个电影
first_n = 10 # <=30 len(urls_suffix)
urls_suffix_first_n = urls_suffix[:first_n]

# 获得所需前10个完整链接的tuple
urls = tuple(f'https://maoyan.com{url_suffix}' for url_suffix in urls_suffix_first_n)

print (urls)

# parse first film page
url_one_film = urls[0]
print(url_one_film)

r_one_film = requests.get(url_one_film,headers=header)
bs_one_film = bs(r_one_film.text, 'html.parser')



