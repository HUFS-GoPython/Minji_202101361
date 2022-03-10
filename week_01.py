###고급파이썬프로그래밍 1주차###

#프로그래밍
    - 프로그래밍 언어를 사용하여 프로그램을 개발하는 것
    - 논리적인 사고 함양 가능
#프로그래밍 언어
    - 프로그램을 개발할 떄 사용하는 도구
    - 인간이 컴퓨터에게 명령할 때 컴퓨터가 이해할 수 있는 언어
#파이썬
    - 쉽고 간결
    - 라이브러리 많음

##Chapter 2. Data: Types, Values, Variables, and Names##

a = 2
- 변수|variable: 특정값을 저장하는 공간
    a
- 값|value
    2
- 할당하다|assign: 변수에 값을 넣는 과정
    "2를 a에 넣었다."
- 자료형|type: 데이터의 형태
    a 데이터 형태: integer(int)
    
    *** a는 2다. a==2 (True)
    
#입력: print(a)
    #출력: 2

a
    2

type(a)
    int

type(2)
    int

type(a==2) #bool, boolean T/F
    bool
    
#Type
    -integer|정수: 1, 2, 3,, (int)
    -floating point number|부동소수점: 1.0, 2.3,, (float)
    -string|문자열: "1", 'apple' (str)
    -boolean|불리언: True/False (bool)
    
type("1")
    str
    
type('apple')
    str
    
type(apple)
    error #변수명
    
type(1.1)
    float
    
#할당
    - '=' 기호 사용
    - 수학에서는 양변이 같다는 의미, 프로그래밍에서는 '할당하다'라는 의미
    - "오른쪽 값을 왼쪽에 할당한다"
    
    -1. 오른쪽에 있는 모든 것은 값을 가져야한다.(초기화 해야한다.)
        x = 4 #초기화
        y = x+3 
        x, y
            (4, 7)
    -2. 같은 변수에 다른 값을 넣을 수 있다. 
        name = 'kim'
        name = 'park'
        name = 4
        print(name) #변수명 동일하게 사용하지 말것
            4
    
#변수명 정하기
    - 나쁜 변수명: 의미없는 것 a, b, c, a1,,
    - 의미있는 이름으로 선언할 것
    - 소문자, 대문자, 숫자, 언더바 사용
        ex)name, name2, my_name, Name,, myName #카멜표기법
      name = 'jenny'
      name1 = 'laura'
      my_name = 'minji'
      print(name, name1, my_name, sep=',')
          jenny, laura, minji
            
    - 안되는 변수명
    1. 숫자로 시작할 수 없다: 11name, 23_name,,
    2. 예약어로 선언할 수 없다: def, False,,
        help("keywords")
            #예약어목록 출력
            
    - 조심할 것: 특별한 용도가 있음
    1. 언더바로 시작하는 변수명: _name
    2. 더블언더바로 시작하는 변수명: __name__
    3. 대문자로 시작하는 변수명: Name
    4. 전체 대문자: NAME
    
#변수명은 대소문자 구분

num = 43
Num = 44
num == Num
    False
    
num = 'number'
Num = 'Number'
num == Num
    False
num!= Num
    True

    
    