# C++ string
> ref) https://chanhuiseok.github.io/posts/algo-37/

---

## string class
-   python, java처럼 **문자열**을 다루기 위한 c++ 클래스
-   문자열 마지막에 **null값 없음**
-   배열처럼 한 문자씩 접근 가능
-   string클래스끼리 합칠 때에는 **+ 연산자** 하나로 가능
-   `<string>` header
```
#include <string>

...
string str1 = "TESTString";
```

## index access
-   str[0] : char형 반환
-   str.at(index) : char형 반환
-   str.front() / str.back() : 맨 앞과 맨 끝 문자 반환

## string length
-   str.size();
-   str.length();

## string - int
-   to_string(num);
```
int a = 7;
string str1;
str1 = to_string(a);    // str1 = "7"
```
-   string to number
```
string str_a = "7"
string str_b = "7.02"
string str_c = "3.14"
string str_d = "2300000000"

int after_a =  stoi(str_a);
double after_b = stod(str_b);
float after_c = stof(str_c);
long int after_d = stof(str_d);
```

## useful function
-   `str.empty();`
:   빈 문자열 확인
-   `swap(str1, str2);`
:   str1과 str2 바꾸기
-   `str.clear();`
:   문자열 비우기
-   `str1.append(str2);`
:   str1 뒤에 str2 추가, str1 += str2와 동일
-   `str.find(str2);`
:   str에서 str2문자열 찾기
-   `str.substr();`
:   문자열의 일부분 반환
```
string str = "TESTtest";
str.substr(3);      // Ttest 반환
str.substr(3, 2)    // Tt 반환
```
-   str간 사전 순서 비교 가능 (<, >, ==)
```
string str1 = "aad";
string str2 = "aaf";

(str1 < str2);  // 1 ( True )
```