from bs4 import BeautifulSoup
# import urllib.request
# import pandas as pd
import requests

# # 크롤링한 결과 저장할 df 만들어놓기
# df = pd.DataFrame(columns=["page_num", "title", "genre", "year", "netflix", "url"])
# count = 0
url = "https://www.4flix.co.kr/board/netflix/7460"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title_year = soup.find_all("h1")[2].text.strip() # 제목(연도) 
title = title_year[:-6] #제목만
year = title_year[-5:-1] #연도만
genre = soup.find_all("h3")[1].text.strip()
netflix = soup.select_one("#card > div.text-block > p").text.strip()
url = soup.select_one("#bo_v_link > ul > button > a")['title']

print(url)
            