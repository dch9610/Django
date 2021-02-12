## 1. 가상환경 설정
    - pip3 install virualenv : 가상환경을 설치함

## 2. 가상환경 이름 설정, 활성화
    - virtualenv 가상환경폴더이름 : 입력하면 가상환경이름에 맞는 폴더 생성
    - source 가상환경폴더이름/bin/activate : 가상환경 활성화

## 3. Django 설치
    - pip3 install django 
    - django-admin startproject 프로젝트명 : 프로젝트 폴더 생성 (코드의 구조를 잡아줌)
    - cd 프로젝트명 -> django-admin startapp 앱이름 : 앱폴더 생성
    
    - app 생성 후 폴더 안에 templates 폴더를 만들어 줘야함
    - 프로젝트명과 동일한 폴더로 들어가 setting.py에서 만들어준 app를 등록해야함

## 4. user app 설정
    - model.py에 들어가 환경설정
    - python3 manage.py makemigrations : 환경설정한 것을 자동으로 만들어줌
    - python3 manage.py migrate : setting에 적용된 app들을 생성해줌
    - sqlite3 db명 : db 확인
    - .schema 테이블명 : 테이블 생성 sql문 확인

    -> db 수정사항이 있으면 makemigration부터 실행하여 적용해줌


## 5. 서버실행
    - python3 manage.py runserver 
    - python3 manage.py createsuperuser : 관리자도구 로그인화면 계정생성