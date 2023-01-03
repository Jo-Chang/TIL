#   git 저장소

>   git : (원격) 분산 버전 관리 시스템

##  `git help`
>   git 명령어들 참조 가능

##  `git init`
>   해당 디렉토리를 git 로컬 저장소로 지정
-   .git 폴더 생성

##  `git add <FileName>`
>   로컬 저장소의 변경 사항 추가
-   변경사항이나 추가된 파일(modified)을 Staged 상태로 변경
-   `git add .` / `git add *` 을 통해 해당 디렉토리 내 파일 한번에 add 가능
-   `git reset HEAD`

##  `git commit -m "message"`
>   커밋
-   add로 staged 된 파일들을 commit상태로 변경

##  `git status`
>   로컬 저장소 내 상태 확인
-   1통 상태 확인

##  `git log`
>   commit log 확인
-   2통 상태 확인
-   Option 
    -   -n          : n개의 히스토리 확인
    -   --oneline   : 한 줄에 commit 내용 확인 (commit id 축약)
    -   --pretty    : 표시할 포맷 설정 ( `--pretty="%H"`로 commit id만 확인 가능)
    - ex) 최근 5개의 commit id만 확인 : `git log -5 --pretty="%H"`
<br>* 위 명령어 --oneline과 함께 사용시 oneline만 적용되었음

##  `git config`
>   git의 기본 설정
-   사용자 환경에서 최초로 git을 commit 할 경우 
    `git config --global user.name "username"`과
    `git config --global user.email "my@email.com"`을 입력하라고 안내함.