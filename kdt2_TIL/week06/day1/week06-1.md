# Week06-1
<link rel="stylesheet" href="../../assets/stylesheets/my_style.css">

-   Two Dimensional List

-----

<br>[Parent Contents...](../../README.md/#til-today-i-learned)

## Contents
- [Two Dimensional List](#two-dimensional-list)

<br>

-----

## Two Dimensional List
-   이차원 리스트 ( Two Dimensional List ) : <span>리스트를 원소</span>로 가지는 리스트

    ```python
    matrix = [[1,2,3], [4,5,6], [7,8,9]]

    print(matrix[0])
    >>> [1, 2, 3]

    print(matrix[1])
    >>> [4, 5, 6]

    print(matrix[2])
    >>> [7, 8, 9]
    ```

    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ```

    ```python
    matrix = []
    for _ in range(10):
        matrix.append([0] * 10)

    matrix2 = [[0] * 10 for _ in range(10)]
    ```

    ```python
    N = 2
    M = 2

    matrix = [[0] * M] * N
    print(matrix)
    # [[0, 0], [0, 0]]
    
    matrix[0][0] = 1
    print(matrix) 
    # [[1, 0], [1, 0]]

    matrix2 = [[0] * M for _ in range(N)]
    print(matrix2)
    # [[0, 0], [0, 0]]
    matrix2[0][0] = 1
    print(matrix2)
    # [[1, 0], [0, 0]]
    ```

- 입력 받기

    ```python
    matrix = []

    for _ in range(8):
        line = list(input())
        matrix.append(line)

    # =
    matrix = [list(input()) for _ in range(8)]
    ```