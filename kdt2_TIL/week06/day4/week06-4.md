# Week06-4

-   Graph


<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

-----

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

## Contents
- [Graph](#graph)
- [Graph Type](#graph-type)
- [Graph Representation](#graph-representation)

<br>

-----


## Graph

-   Graph : <span>정점(Vertex)</span>와 이를 연결하는 <span>간선(Edge)</span>들의 집합으로 이루어진 비선형 자료구조

-   정점 ( Vertex ) : 간선으로 <span>연결되는 객체</span>, 노드(Node)라고도 불림
-   간선 ( Edge ) : 정점 간의 <span>관계(연결)</span>를 표현하는 선
-   경로 ( Path ) : <span>시작</span> 정점부터 <span>도착</span> 정점까지 거치는 정점을 나열한 것
-   인접 ( Adjacency ) : 두 개의 정점이 하나의 <span>간선으로 직접 연결</span>된 상태


-----


## Graph Type

-   무방향 그래프 ( Undirected graph ) : 간선의 <span>방향이 없는</span> 그래프
    +   차수 ( Degree ) : 하나의 정점에 연결된 간선의 개수
    +   간선을 통해 양방향의 정점 이동 가능
    +   모든 정점의 차수의 합 = 간선 수 X 2

-   유방향 그래프 ( Directed graph ) : 간선의 <span>방향이 있는</span> 그래프
    +   간선의 방향이 가리키는 정점으로 이동 가능
    +   차수 ( Degree ) : 진입 차수와 진출 차수로 나누어짐


-----


## Graph Representation

-   인접 행렬 ( Adjacent matrix ) : 간선이 있으면 1, 없으면 0으로 표현되는 <span>행렬</span>

    ![인접 행렬](assets/01.png)


-   인접 리스트 ( Adjacent list ) : <span>리스트</span>를 통해 인접 정점들을 순차적으로 표현

    ![인접 리스트](assets/02.png)