# 파이썬(3.8.10) 을 활용하여 로그를 Slack app 확인할수 있는 코드입니다.

<!--
**nis1130/nis1130** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

## 서버 사양
- 운영체제 : Linux
- 운영체제의 : 상세정보 Linux-5.13.0-1022-aws-x86_64-with-glibc2.29
- 운영체제 버전 : #24~20.04.1-Ubuntu SMP Thu Apr 7 22:10:15 UTC 2022
- 프로세서 : x86_64
- cpu수 : 1

## Ubuuntu 서버 명령어 
- (*추가)한국 기준으로 서버 시간 설정: sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
- 실행 : python3 API_slack.py or ./API_slack.py
- sudo apt-get update

### python module 설치

- python3 -m pip install slacker
- python3 -m pip install request

## 실행 예시
- "/var/log/syslog.1" : 검색할 파일
- "Fail" : 검색할 문자(열)

![ERROR_LOG](https://user-images.githubusercontent.com/102892765/166687620-d2800c01-6dfb-4ce7-9bbf-ed9bab1bb411.png)

## 실행 화면

- Web

![로그](https://user-images.githubusercontent.com/102892765/166688681-642bb259-c7f2-45c6-8af8-f9ffda74259f.png)

- App 

![KakaoTalk_20220504_221747689](https://user-images.githubusercontent.com/102892765/166689981-e7fcec56-23be-45f8-96b0-ba1e8fe00e97.jpg)


