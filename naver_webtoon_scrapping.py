import requests
from bs4 import BeautifulSoup
import csv
import re

naver_wt_URL = 'https://comic.naver.com/webtoon/weekday.nhn'

naver_response = requests.get(naver_wt_URL)

soup = BeautifulSoup(naver_response.text,'html.parser')

naver_wts = soup.select('#content > div.list_area.daily_all > div.col')

naver_wt_names = []
naver_wt_days = []
naver_wt_ids = []

for naver_wt in naver_wts:
    naver_wt_id = naver_wt.select( 'div.col_inner > ul > li > a')
    for info in naver_wt_id:
        naver_wt_ids.append(info['href'].split('&')[-2].split('=')[-1])
        naver_wt_days.append(info['href'].split('=')[-1])
        naver_wt_names.append(info.text)

# print(naver_wt_names)

naver_wt_intro = []

for i in range(len(naver_wt_names)):
    naver_wt_id = naver_wt_ids[i]
    naver_wt_day = naver_wt_days[i]
    naver_detail_URL = 'https://comic.naver.com/webtoon/list.nhn?titleId='+naver_wt_id+'&weekday='+naver_wt_day
    naver_detail_response = requests.get(naver_detail_URL)
    soup = BeautifulSoup(naver_detail_response.text, 'html.parser')
    naver_intros = soup.select('#content > div.comicinfo > div.detail > p')
    naver_intros = re.sub("<.*?>", " ", str(naver_intros))
    naver_intros = naver_intros.replace('[',' ').replace(']', ' ').strip()
    naver_wt_intro.append(naver_intros)


naver_webtoon = {}

for i in range(len(naver_wt_names)):
    naver_webtoon[naver_wt_names[i]] = naver_wt_intro[i]

with open('naver_webtoon.csv', 'w', newline='',encoding='utf-8-sig') as file:
  writer = csv.DictWriter(file, fieldnames = ['name', 'intro'])
  for key in naver_webtoon.keys():
      writer.writerow({'name' : key, 'intro' : naver_webtoon[key]})

