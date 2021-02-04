 # -*- coding: utf8 -*-

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
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT,\
#             email TEXT, phone TEXT, website TEXT, regdate TEXT)")

# 데이터 삽입
# ?는 튜플형태로 만든값이 들어감

c.execute("INSERT INTO users VALUES(1,'Lee','dch9610@naver.com','010-2020-2021',\
           'www.naver.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",
(2,'Park','Park@naver.com','010-1111-1111','Park.com',nowDatetime))

# # 많은 데이터 삽입 (튜플, 리스트형태)
userList = (
    (3, 'Lee', 'Lee@naver.com','010-2222-2222','Lee.com',nowDatetime),
    (4, 'Joe', 'Joe@naver.com','010-3333-3333','Joe.com',nowDatetime),
    (5, 'You', 'You@naver.com','010-4444-4444','You.com',nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
                VALUES (?,?,?,?,?,?)", userList)


# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")

# 지워진 결과값 반환
# print("users db delete :", conn.execute("DELETE FROM users").rowcount)


# 커밋 : isolation_level = None일 경우 자동 반영 (오토 커밋)
# conn.commit() 을 작성해야 반영

# 롤백 : 원하는 위치를 되돌리기 위함
# conn.rollback()  

# 접속 해제
conn.close()