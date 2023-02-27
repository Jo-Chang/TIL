# Week10-1

-   Positioning for CSS layout


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

-----


## Position

- CSS Position : Normal Flow에서 요소를 끄집어내서 다른 위치로 배치하는 것
  > 다른 요소 위에 놓기, 화면 특정 위치에 고정시키기 등

- z-index : 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
  + 요소 값이 큰 객체가 위에 표현

- Position 유형
  + static
  + relative
  + absolute
  + fixed
  + sticky

- static
  + 기본값
  + 요소를 Normal Flow에 따라 배치

- relative
  + 요소를 Normal Flow에 따라 배치
  + 자기 자신을 기준으로 이동
  + 요소가 차지하는 공간은 static일 때와 같음

- absolute
  + 요소를 Normal Flow에서 제거
  + 가장 가까운 relative 부모 요소를 기준으로 이동
  + 문서에서 요소가 차지하는 공간이 없어짐

- fixed
  + 요소를 Normal Flow에서 제거
  + 현재 화면영역(viewport)을 기준으로 이동
  + 문서에서 요소가 차지하는 공간이 없어짐

- sticky
  + 요소를 Normal Flow에 따라 배치
  + 가장 가까운 block 부모 요소를 기준으로 이동
  + 요소가 특정 임계점(ex. viewport의 상단으로부터 10px)에 스크롤될 때 그 위치에서 고정됨(fixed)
  + 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
    * 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문

