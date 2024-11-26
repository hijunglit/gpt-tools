# python for gpt

# 강의 듣고 목표: 스크래퍼 프로그램 만들기

### data structure

1. mutable
   - 변경 가능한.
   - 사용법: []
2. tuple
   - 변경 불가능
   - 사용법: ()
3. dictionary
   - 복잡한 데이터
   - mutable(변경 가능)

- python standard library : 파이썬에 내장되어 있는 기본 라이브러리 모음
- PIPY : 다른 사람들이 만들 라이브러리

  24.11.7

### OOP(Object Oriented Programming)

_self_ : class 안에 있는 모든 메소드에게 줘야하는 인자

1. 코드를 구성하는 규칙. 패러다임
2. 직관적이다.
3. 함수 캡슐화
4. method:
   - **init**()
   - **str** : class를 출력할 때 python에 의해 호출된다.
5. inheritance: 코드의 반복을 줄여준다.(중복)

   - super() : 부모의 class 를 참조함을 의미한다. 따라서 부모의 **init** 메소드를 호출한다.

     24.11.10

6. 객체 지향 접근 방식으로 프로그램을 모델링 하는 것은 정말 쉽다.
   우리는 객체 지향 세상에 살고 있으며 우리가 사용하는 모든 것들, 사람, 사회 구조
   아주 쉬운 방법을 객체를 대표할 수 있다.

### job scrapper

1. beautifulsoup4
   - html을 탐색할 수 있게 해주는 라이브러리
2. 변수에서 언더바(\_)넣는 것은 유효한 variable이다.
3. unpack
4. len() = 배열의 길이를 반환, find_all() = 배열을 반환
5. range() : 숫자를 넣어주면 그 숫자만큼 for loop를 실행시켜준다.
