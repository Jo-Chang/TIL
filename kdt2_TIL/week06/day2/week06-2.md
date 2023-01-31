# Week06-2
<link rel="stylesheet" href="../../css/my_style.css">

-   Two Dimensional List 2

-----

<br>[Parent Contents...](../../../README.md/#til-today-i-learned)

## Contents
- [Circuit](#circuit)

<br>

-----


## Circuit

-   순회

    ```python
    matrix = [
        [0, 5, 3, 1],
        [4, 6, 10, 8],
        [9, -1, 1, 5]
    ]

    max_value = max(map(max, matrix))
    min_value = min(map(min, matrix))

    print(max_value)
    print(min_value)
    ```


-----


## Transpose

-   전치 ( Transpose ) : 행과 열을 맞바꿈

    ```python
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 1, 2]
    ]

    transposed_matrix = [[0] * 3 for _ in range(4)]

    for i in range(4):
        for j in range(3):
            transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
    ```

-----

## Rotation

-   회전 ( Rotation )

    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    n = 3
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[j][n-i-1]
    ```