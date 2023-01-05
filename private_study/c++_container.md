# C++ Containers
> ref) https://blockdmask.tistory.com/70
## Contents
- [vector](#vector)
- [set](#set)
<br>----- tips -----
- [algorithm](#algorithm)

---

## vector
-   vector container 
: 자동으로 메모리가 할당되는 배열
    - C에서 사용자가 직접 동적할당하고 해제하는 배열로 이해하자!
-   <vector> header에 포함
-   How-to use
    -   선언 방법 `vector<{Data Type}> {var name}`
    -   `vector<{Data Type}> {var name}(n, m)`    --> n개의 m원소를 가진 벡터로 초기화
    -   `vector[idx]` : <tab>해당 index 위치에 삽입
    -   `vector.push_back(num)` : 마지막 위치에 삽입
    -   `vector.erase(iter)` : iter가 가리키는 원소 제거
        - -- size만 줄어들고 capacity(할당된 메모리) 그대로 유지
    -   `vector.pop_back()` : 마지막 위치 원소 제거
    -   `vector.front() / vector.back()`  : 첫번째 / 마지막 원소
    -   `vector.begin() / vector.end()`   : 첫번째 / 마지막 원소의 iterator
    -   `vector.clear()`  : 벡터 비우기
    -   `vector.size()`   : 백터 크기 반환

---

## set
-   set container : 노드 기반 컨테이너로 key값으로 이루어진 균형 이진트리로 구현 -> key값이 중복되지 않음!!
    - vector를 쓰다가 중복값을 허용하고 싶지 않을때 사용해보자!
-   <set> header에 포함
-   선언 방법 set<{Data Type}> {var name}

---

## Tips)
## algorithm
-   <algorithm> header 내부에 Container들과 사용하기 좋은 유용한 함수들 구현
    - sort(iter-begin-, iter-end-, {custom function()}) : Container 시작점과 끝점을 기준으로 기본적으로 오름차순으로 정렬