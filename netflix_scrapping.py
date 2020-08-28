from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# 크롤링한 결과 저장할 df 만들어놓기
df = pd.DataFrame(columns=["page_num", "title", "genre", "year", "netflix","link"])
count = 0

# 크롤링
for num in range(1,8000):
    url = "https://www.4flix.co.kr/board/netflix/" + str(num)
    with urllib.request.urlopen(url) as url:
        try:
            doc = url.read()
            soup = BeautifulSoup(doc, "html.parser")

            title_year = soup.find_all("h1")[2].text.strip() # 제목(연도) 
            title = title_year[:-6] #제목만
            year = title_year[-5:-1] #연도만
            genre = soup.find_all("h3")[1].text.strip()
            netflix = soup.select_one("#card > div.text-block > p").text.strip()
            link = soup.select_one("#bo_v_link > ul > button > a")['title']

            df.loc[num] = [num, title, genre, year, netflix,link]
            count+=1
            print(num)
        except:
            print("except",num)
            pass #3039는 글 지워짐
        #text
    df.to_csv('movie_project.csv', index=False, encoding='utf-8')


print(df)
df.to_csv('movie_project.csv', index=False, encoding='utf-8')