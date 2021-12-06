import pymysql
import requests 
from bs4 import BeautifulSoup

# 인터프리터에서 직접 실행된 경우
if __name__=="__main__":
    rank = 100
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    req = requests.get("https://www.melon.com/chart/index.htm", headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')
    
    titles = soup.find_all("div", {"class":"ellipsis rank01"})
    singers = soup.find_all("div", {"class":"ellipsis rank02"})
    
    title = []
    singer = []
    
    for t in titles:
        title.append(t.find('a').text)
        
    for s in singers:
        singer.append(s.find('span',{'class':'checkEllipsis'}).text)
    items = [item for item in zip(title,singer)]
    


conn = pymysql.connect(
    user='mikey', 
    passwd='xxx123', 
    host='127.0.0.1', 
    db='hj',
    charset='utf8'
)

cursor = conn.cursor()

# 실행할 때 다른 값 나오지 않게 테이블 제거
cursor.execute("DROP TABLE IF EXISTS melon")

# 테이블 생성
sql = "CREATE TABLE melon (ran int, title text, url text)"
cursor.execute(sql)

# 데이터 저장
i = 1
for item in items:
    cursor.execute(f"INSERT INTO melon VALUES({i},\'{item[0]}\',\'{item[1]}\')")
    i +=1
    
conn.commit()
conn.close()