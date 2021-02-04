 # -*- coding: utf8 -*-

# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time
# 사운드 출력 필요 모듈
import pygame # 맥에서 사용
# import winsound # 윈도우에서 사용

import sqlite3
import datetime

# 사운드 설정
pygame.mixer.init()
pass_sound = pygame.mixer.Sound("sound/good.wav")
wrong_sound = pygame.mixer.Sound("sound/bad.wav")




# DB생성 & 오토 커밋
# 본인 DB경로
conn = sqlite3.connect('resource/records.db', isolation_level=None)

# Cursor
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(\
    id INTEGER PRIMARY KEY AUTOINCREMENT, \
    cor_cnt INTEGER,\
    record text, \
    regdate text) \
    ")







words = []       # 영어 단어 리스트(1000개 로드)

n = 1           # 게임 시도 횟수
cor_cnt = 0     # 정답 개수

with open('word.txt','r') as f:
    for c in f:
        words.append(c.strip())

# print(words) # 단어 리스트 확인

input("Ready? Press Enter Key!") # Enter Game Start!


start = time.time() # 시작시간


# 
while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print() # 줄 바꿈

    print("*Question #{}".format(n))
    print(q) # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip(): # 입력확인 공백제거
        print("Pass!")
        # 정답소리 재생
        pass_sound.play() # 맥용
        # winsound.PlaySound('sound/good.wav', winsound.SND_FILENAME) # 윈도우
        cor_cnt += 1
    else:
        # 오답소리 재생
        wrong_sound.play() # 맥용
        # winsound.PlaySound('sound/bad.wav', winsound.SND_FILENAME) # 윈도우 
        print("Wrong!")

    n+=1 # 다음 문제 전환

end = time.time() # End time
et = end - start  # 총 게임 시간
et = format(et, ".3f") # 소수 3자리 출력

if cor_cnt > 3:
    print("합격")
else:
    print("불합격")


# 결과 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record','regdate') VALUES (?,?,?)",
        (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) )



# 수행시간 출력
print('게임시간 :',et,"초","정답 개수: {}".format(cor_cnt))


# 시작 지점
if __name__ == '__main__':
    pass









