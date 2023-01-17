# API
-   usually JSON format..

-----

## Client side
-   Request
    +   **C**REATE  : POST
    +   **R**EAD    : GET
    +   **U**PDATE  : PUT(all) / PATCH(part)
    +   **D**ELETE  : DELETE

-----

## Server side
-   Response

-----

## RESTful API
-   RESTful API (Representational State Transfer Application Programming Interface) : 체계적인 API 구조
    >   [Understanding the REST Style, 2000, Roy Fielding](assets/Roy_T._Fielding_Understanding_the_REST_Style.pdf)
    <br>[**link..**](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
-   Result state
    +   Good - 200
    +   Bad - 400(Request Error - client), 500(Response Error - server)
    >   ex) 404 - Client측의 잘못된 요청

-----

## API Documents
-   API 사양 명세서
    >   [네이버 로그인 Open API **link..**](https://developers.naver.com/docs/common/openapiguide/apilist.md#%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%B0%A9%EC%8B%9D-%EC%98%A4%ED%94%88-api)

-----

## API Data Format - JSON
-   비닐 봉투(API) 내용물(<span style="color:#FF5353">data</span>)의 형식(<span style="color:#FF5353">format</span>) 중 하나!
    > *.json, *.xml, ...
    ```json
    {
        키1(Key): 값1(Value),
        키2(Key): 값2(Value),
        키3(Key): [ 값3, 값4, 값5 ], // 배열
    }
    ->
    {
        "category": "음료", 
        "sort": "desc",
        "items": [ "카페 모카", "카페 라떼", "아메리카노" ]
    }
    ```