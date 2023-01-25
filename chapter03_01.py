# Chapter03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형[list, tuple, collections.deque]
# Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview]
# 컨테이너와 Flat의 속도차이는 당연히 한 개의 자료형만을 저장하는 Flat이 performence가 좋다.

# 가변(Mutable) : list, bytearray, array.array, momoryview, collections.deque
# 불변(Imutable) : tuple, str, bytes

# 지능형 리스트(Comprehending Lists) -> 리스트 컴프리헨션
# None Comprehending List와 Comprehending List의 속도 차이는 Comprehending List가 조금더 우세하다고 한다.

# None Comprehending Lists

chars = '!@#$%^&*()_+'
code1 = []

for s in chars:
    code1.append(ord(s))

print('EX1-1 -', code1)

# Comprehending Lists
# 속도 약간 우세
codes2 = [ord(s) for s in chars]
print('EX1-2 -', codes2)

codes3 = [ord(s) for s in chars if ord(s) > 40]
print('EX1-3 -', codes3)

# Comprehending Lists + Map, Filter
codes4 = list(map(ord, chars))
print('EX1-4 -', codes4)

codes5 = list(filter(lambda x : x > 40, map(ord, chars)))
print('EX1-5 -', codes5)

print('EX1-6 -', [chr(s) for s in codes2])
print('EX1-6 -', [chr(s) for s in codes3])
print('EX1-6 -', [chr(s) for s in codes4])
print('EX1-6 -', [chr(s) for s in codes5])

print()
print()

# Generator

import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X) -> 일괄 생성하지 않기 때문에 성능상으로 압도적으로 좋다.
# 리스트의 원소가 100만개라면 100만개가 모두 메모리에 올라간다. 하지만 generator는 그렇지 않다.
# 많은 데이터가 있을 경우라면 generator를 사용하는 것이 훨씬 유리하다.
# 하지만 경우에 따라서는 리스트를 사용해야 하는 경우도 있다.
tuple_g = (ord(s) for s in chars) # 소괄호를 이용해서 list comprehention 처럼 사용을 하면 generator가 생성이 된다.

print('EX2-1', tuple_g)
print('EX2-2 -',  next(tuple_g))
print('EX2-3 -',  next(tuple_g))

# Array -> array는 내부적으로 많이 사용된다.
array_g = array.array('I', (ord(s) for s in chars))

print('EX2-4 -', array_g)
print('EX2-5 -', array_g.tolist())

print()
print()

# 제네레이터 예제
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print('EX3-2 -', s)

print()
print()

# 리스트 주의 할 점 -> 해깔리는 문제이다.
marks1 = [['~'] * 3 for n in range(3)] # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks2 = [['~'] * 3] * 3               # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

print('EX4-1 -', marks1) # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print('EX4-2 -', marks2) # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
# marks1과 marks2는 를 찍어보면 동일한 값이 나오기 때문에, 똑같다고 생각할 수 있지만, marks1과 marks2는 큰 차이점이 있다. -> 이거를 파악해야 한다.

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1) # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~']]
print('EX4-4 -', marks2) # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]

# 증명
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2])

# Tuple Advanced

# Packing & Unpacking
a, b = divmod(100, 9) # a->몫, b->나머지
print(a, b)

print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9)))
print('EX5-3 -', *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
print(type(rest)) # 이 경우의 rest의 타입은 list이다.

x, y, *rest = range(2)
print('EX5-5 -', x, y, rest) # 0 1 [] 
print(type(rest))

x, y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x, y, rest) # 1 2 [3, 4, 5]
print(type(rest))

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, m, id(l), id(m))

l = l * 2 # 새로운 객체 생성
m = m * 2 # 새로운 객체 생성

print('EX6-2 -', l, m, id(l), id(m))

l *= 2 # 새로운 객체 생성
m *= 2 # 리스트인경우 복합대입연산자를 사용하면 자기 자신한테 재할당을 한다. 즉, ID값이 변하지 않는다. -> 자기 자신을 수정하다.

# 자기 자체에서 재할당이 이루어지는 것과, 새로운 객체를 생성한다는 개념을 잘 알아야한다.
# 새로운 객체를 생성한다는 것은 그만큼 메모리 사용량이나, 리소스를 잡아 먹는다는 의미이다.

print('EX6-3 -', l, m, id(l), id(m))

print()

# sort vs sorted
# 옵션 : reverse, key=len, key=str.lower, key=str.upper, key=func
# 정렬은 정말 중요하다.
# 알고리즘 시험에서도 정렬은 반드시 정복해야 한다.

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 '새로운' 객체 반환 -> 원본은 변경되지 않는다.

test = sorted(f_list)
print(test)
print(f_list)

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
print('EX7-3 -', sorted(f_list, key=len))
print('EX7-4 -', sorted(f_list, key=str.lower))
print('EX7-5 -', sorted(f_list, key=str.upper))
print('EX7-6 -', sorted(f_list, key=lambda x : x[-1])) # 단어의 끝 글자를 기준으로 정렬
print('EX7-7 -', sorted(f_list, key=lambda x : x[-1], reverse=True))

print('EX7-6 -', f_list)

print()

# sort : 정렬 후 객체 직접 변경
# 반환 값 확인 : None을 리턴하면 반환값이 없다라는 의미이다.
# 만약에 어떤 함수가 None을 반환했다면, 이 함수는 객체를 직접 변경하는 함수라고 어느정도는 추측할 수 있다.

a = f_list.sort()
print(a, f_list)

print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x : x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x : x[-1], reverse=True), f_list)