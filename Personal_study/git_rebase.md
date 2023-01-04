<!--
ref) https://devhealer.tistory.com/53
-->

1.  `$git log`
    - commit log 확인
2.  `$git rebase -i {hash}`
    - 수정하고 싶은 날짜의 commit hash 복사
3.  `$git commit --ammed --no edit --date="{조작하고 싶은 날짜}"
    - 날짜 지정
4.  `$git rebase -- continue`
    - rebase 진행
5.  `git push -f origin master`
    - 강제 푸쉬(-f option)을 사용해 수정한 rebase 내용 등록

**본 md파일은 실시간 20분에 commit하여 22분으로 등록될 예정임