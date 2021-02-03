# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite3 
print('sqlite3.version', sqlite3.version)
print('sqlite3.sqite_version', sqlite3.sqlite_version)


# DB 생성 & Auto Commit (영구적으로 반영할때 Commit을 사용), Rollback은 되돌리기
conn = sqlite3.connect('resource/database.db', isolation_level=None)

# Cursor 
c = conn.cursor()
print('Cursor Type: ', type(c))


# 테이블 생성 (Data Type : Text, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT,\
            email TEXT, phone TEXT, website TEXT, regdate TEXT)")

# 데이터 삽입
# ?는 튜플형태로 만든값이 들어감
c.execute("INSERT INTO users VALUES(3,'Lee','dch9610@naver.com','010-2020-2021',\
            'www.naver.com', ?)", (nowDatetime,))