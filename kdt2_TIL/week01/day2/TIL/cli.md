# CLI
>   CLI : Command Line Interface

## `echo 'string'`
>   cli에 string 출력

## `pwd`
>   현재 디렉토리 경로 출력

## `cd <directory name>`
>   해당 디렉토리로 이동

## `ls`
>   현재 디렉토리 내부 파일 목록 호출
-   Option
    -   -l  : 파일의 세부정보 표시
    -   -R  : 파일 내부 파일 표시
    -   -a  : 숨겨진 파일 표시

## `mkdir <directory name>`
>   폴더 생성

## `touch <file name>`
>   파일 생성

## `rm <file name>`
>   파일과 폴더 제거
-   일반적으로는 폴더는 제거되지 않음
-   Option
    -   -d      : 디렉토리 제거 (디렉토리 내부에 파일이나 폴더 존재시 제거X)
    -   -f      : 파일 권한에 관계없이 확인 프롬트 없이 파일 제거 시도
    -   -r/-R   : 디렉토리 제거 (루트 디렉토리를 제거하므로 내부 파일 여부 상관없이 삭제 진행)