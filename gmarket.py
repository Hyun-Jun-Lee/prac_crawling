import pymysql
import requests
from bs4 import BeautifulSoup

conn = pymysql.connect(
    user='mikey', 
    passwd='xxx123', 
    host='127.0.0.1', 
    db='hj',
    charset='utf8'
)

cursor = conn.cursor()

sql = ''' CREATE TABLE items ( item_code VARCHAR(20) NOT NULL PRIMARY KEY, title VARCHAR(200) NOT NULL, ori_price INT NOT NULL, dis_price INT NOT NULL, dis_percent INT NOT NULL, provider VARCHAR(100) ); '''

cursor.execute(sql)

sql = ''' CREATE TABLE ranking ( num INT AUTO_INCREMENT NOT NULL PRIMARY KEY, main_category VARCHAR(50) NOT NULL, sub_category VARCHAR(50) NOT NULL, item_ranking TINYINT UNSIGNED NOT NULL, item_code VARCHAR(20) NOT NULL, FOREIGN KEY (item_code) REFERENCES items(item_code) ); '''

cursor.execute(sql) 

conn.commit() 
conn.close()

# 크롤러

conn = pymysql.connect(
    user='mikey', 
    passwd='xxx123', 
    host='127.0.0.1', 
    db='hj',
    charset='utf8'
)

conn.cursor()

# gmarket best main page
res = requests.get("http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G01")
soup = BeautifulSoup(res.content, 'html.parser')

# 카테고리 목록
categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories[:2]:
    get_category("http://corners.gmarket.co.kr"+category['href'], category.get_text())
