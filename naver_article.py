import pymysql

conn = pymysql.connect(
    user='mikey', 
    passwd='{설정한 비밀번호}', 
    host='127.0.0.1', 
    db='hj', # 연결할 DB 이름
    charset='utf8'
)