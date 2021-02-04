# -*- coding: utf8 -*-
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제
import sqlite3

# DB생성(파일)
conn = sqlite3.connect('resource/database.db')

# 커서 연결
c = conn.cursor()

# # 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id =?",('niceman',2))
# conn.commit()

# # 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id",{'name':'goodman','id':5})
# conn.commit()

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s' " % ('badboy',3))
# conn.commit()

# 중간 데이터 확인1
# for user in c.execute("select * from users"):
#     print(user)


# Row Delete1
# c.execute("delete from users where id = ?",(2,))
# conn.commit()

# Row Delete2
# c.execute("delete from users where id = :id",{"id":5})
# conn.commit()

# Row Delete3
# c.execute("delete from users where id = '%s'" % 4)
# conn.commit()

# 중간 데이터 확인2
# for user in c.execute("select * from users"):
#     print(user)

# 테이블 전체 데이터 삭제
print('users db deleted:', conn.execute("delete from users").rowcount, "rows")
conn.commit()

# 접속 해제
conn.close()