 # -*- coding: utf8 -*-

# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 생성)
conn = sqlite3.connect('resource/database.db') # 본인 DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("select * from users")

# # 커서 위치가 움직이면서 해당 값에 대한 데이터 출력
# # 1개 로우 선택
# print('One -> \n', c.fetchone())

# # 지정 로우 선택
# print('Three ->', c.fetchmany(3))

# # 전체 로우 선택
# print('All ->', c.fetchall())

# # 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retriew1 > ', row)

# # 순회2
# for row in c.fetchall():
#     print('retriew2 > ', row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retriew3 > ', row)


# WHERE Retrieve1
# 튜플 형식 바인딩
# param1 = (3,)
# c.execute("SELECT * FROM users WHERE id=?",param1)
# print('param1', c.fetchone())
# print('param1', c.fetchall()) # 데이터 없음

# WHERE Retrieve2
# 값 그대로 바인딩
# param2 = 4
# c.execute("SELECT * FROM users WHERE id='%s'" % param2)
# print('param2', c.fetchone())
# print('param2', c.fetchall()) # 데이터 없음

# WHERE Retrieve3
# 딕셔너리로 바인딩
# c.execute("SELECT * FROM users WHERE id=:Id", {"Id":5})
# print('param', c.fetchone())
# print('param', c.fetchall()) # 데이터 없음

# WHERE Retrieve4
# param3 = (3,5)
# c.execute("SELECT * FROM users WHERE id IN(?,?)", param3)
# print('param3', c.fetchall())

# WHERE Retrieve5
# c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (1,3))
# print('param5', c.fetchall())

# WHERE Retrieve5
# c.execute("SELECT * FROM users WHERE id=:Id1 OR id=:Id2", {"Id1":2,"Id2":4} )
# print('param6', c.fetchall())

# Dump 출력 (DB를 백업)
with conn:
    with open('resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
        print('Dump Print Complete')










