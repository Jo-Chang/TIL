# Python Web Crawling


<style>
    span { color: #FF5353; }
</style>

>   ref) https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%AC%EB%A1%A4%EB%A7%81-%EA%B8%B0%EC%B4%88/unit/92371


### *Caution*

-   상업적 목적으로 이용하지 말것
-   대상 사이트에 과도한 트래픽을 주지 말것


-----


## HTML tags

|**Tag**|**Role**|
|:---:|:---:|
|div|구역 나누기|
|a|링크|
|h1|제목|
|p|문단|
|ul, li|list|


-----


## Requests

-   <span>HTTP 통신</span>을 위한 파이썬 라이브러리

    ```python
    import requests

    response = requests.get("https://www.naver.com")
    html = response.text
    print(html)

    # RaiseConnection  -> requests 제대로 안 될 경우 Error
    ```

-----


## BeautifulSoup

-   bs4 ( BeautifulSoup )
-   내가 원하는 태그 선택
-   HTML 분석을 위한 파이썬 라이브러리
-   `Beautifulsoup(html 코드, html 번역)`

    ```python
    import requests
    from bs4 import Beautifulsoup

    # 네이버 시작페이지 로드, 네이버 서버에 대화 시도
    response = requests.get("https://www.naver.com")
    # 네이버에서 받은 response를 html 형식으로 변환
    html = response.text
    # 네이버 시작페이지 html을 soup 형식으로 변환
    soup = Beautifulsoup(html, 'html.parser')
    # 원하는 영역의 태그로 원하는 내용 추출
    word = soup.select_one("#NM_set_home_btn")
    # 원하는 내용(텍스트)만 영역에서 추출
    print(word.text)
    ```

-----

## CSS 선택자

-   CSS : 웹사이트의 디자인을 표시하기 위한 언어
    +   글자 색, 폰트 크기, 가로 세로 길이 변경 등
-   디자인을 변경한 HTML 태그 선택
-   종류
    +   태그 선택자 : 태그의 이름으로 선택
    >   h1, a
    +   id 선택자 : id 값

    |<center>HTML</center>|선택자|
    |:---|:---:|
    |`<div id ="articleBody">`<br>&nbsp;`본문 내용...`<br>`</div>`|<span style="color:#5353FF;">#</span>articleBody|

    +   class 선택자 : class 값으로 선택

    |<center>HTML</center>|선택자|
    |:---|:---:|
    |`<div class ="info_group">`<br>&nbsp;`뉴스 목록...`<br>`</div>`|<span style="color:#5353FF;">.</span>info_group|

    +   자식 선택자 : 내가 원하는 태그에 <span>별명이 없을 때</span> 사용

    |<center>HTML</center>|선택자|
    |:---|:---:|
    |`<div class ="logo_sports">`<br>&nbsp;`<span>뉴스 목록...</span>`<br>`</div>`|.logo_sports <span style="color:#5353FF;">></span> span|
    |`<div class ="logo_sports">`<br>&nbsp;`<span>뉴스 목록...</span>`<br>`</div>`|.news_headline <span style="color:#5353FF;">></span> h4|