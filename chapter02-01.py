# Chapter02-1
# 파이썬 심화
# 데이터 모델(Date Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬 데이터를 추상화
# 모든 객체 -> id, type -> value
# 파이썬 -> 일관성

# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_leng1 = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
print('Ex1-1 -', line_leng1)


# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point1', 'x y')

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)

# 출력
print('Ex1-2 -', line_leng2)
print('Ex1-3 -', line_leng1 == line_leng2)

# 네임드 튜플 선언 방법
# Point = namedtuple('Point', 'x y')
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
# south korea는 하나의 속성인데, 띄어쓰기 때문에 속성이 2개로 나뉜다. 이런경우는 콤마를 사용해서 명시적으로 알려준다.
# Point3 = namedtuple('Point', 'south korea') 
Point3 = namedtuple('Point', 'x y')
# 중복된 속성이나, 속성의 이름이 파이썬의 예약어(키워드)인 경우에 rename 옵션을 True로 설정하여 이름을 자동으로 변경해준다.
Point4 = namedtuple('Point', 'x y x class', rename=True) # rename의 default값은 False이다.

# 출력
print('EX2-1 -', Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3

# Dict to Unpacking
temp_dict = {'x':75, 'y': 55}
p5 = Point3(**temp_dict)

# 출력
print(p1) # Point(x=10, y=35)
print(p2) # Point(x=20, y=40)
print(p3) # Point(x=45, y=20)
print(p4) # Point(x=10, y=20, _2=30, _3=40)
print(p5) # Point(x=75, y=55)

print()
print()

# 사용
print('EX3-1 -', p1[0] + p2[1]) # namedtuple은 일반 tuple처럼도 사용가능 # Index Error 주의
print('EX3-2 -', p1.x + p2.y) # 클래스 변수 접근 방식

# Unpacking
x, y = p3
print('EX3-3 -', x + y)

# Rename 테스트
print('EX3-4 -', p4)

print()
print()

# 네임드 튜플 메소드
# -> 강의에서 다룬 namedtuple method가 공식 reference에 나와있는 거의 대부분의 함수를 다룬거다.

temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print('EX4-1 -', p4)

# _fields() : 필드 네임 확인
print('EX4-2 -', p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환 -> 강의에서는 OrderedDict을 반환했지만, 나는 그냥 dict을 반환했다.
print('EX4-3 -', p1._asdict(), p4._asdict())

# _replace() : 수정된 '새로운' 객체 반환 -> 튜플은 불변형이기 때문에...

print('EX4-4 -', p2._replace(y=100))

print()
print()

# TIP) tuple은 list보다 빠르다 -> tuple은 불변이기 때문에 수정, 삭제가 불가능한 반면 list는 가능해서 tuple이 상대적으로 가볍다

# 실 사용 실습
# 학생 전체 그룹 생성
# 반20명, 4개의 반 -> (A, B, C, D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = ' A B C D'.split() # ['A', 'B', 'C', 'D']

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print('EX5-1 -', len(students))
print('EX5-2 -', students)

print()
print()

# 가독성X
students2 = [Classes(rank, str(number)) 
                    for rank in 'A B C D'.split() 
                        for number in range(1,21)]
print('EX6-1 -', len(students2))
print('EX6-2 -', students2)

print()
print()

# 출력
for s in students:
    print('EX7-1 -', s)