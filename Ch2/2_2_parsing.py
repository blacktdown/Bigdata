"""
날짜 : 2020/12/28
이름 : 박준우
내용 : 파이썬 HTML 페이지 파싱(Parsing)하기

Parsing
 - 문서 해독을 의미하는 용어(사전적 의미)
 - 마크업문서(HTML, XML)에서 특정 태그의 데이터를 추출하는 처리과정
"""
import requests as req
from bs4 import BeautifulSoup as bs

# 페이지 요청
response = req.get('https://news.daum.net')

# HTML Parsing
dom = bs(response.text, 'html.parser')
titles = dom.select('.list_issue .tit_thumb > a')

# 데이터 출력
for tit in titles:
    print(tit.text)