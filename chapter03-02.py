# Chapter03-2
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# Dict 구조
print("EX1-1 -")
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

# 가변(mutable) 인지, 불변(immutable)인지를 확인하려면 hash값을 확인해보면된다. 
# -> 가변은 hash값이 없고, 불변은 hash값이 있다.
print('EX1-2 -', hash(t1))
# print('EX1-3 -', hash(t2)) # 리스트는 중복을 허용하는 거기때문에 hash가 필요없다.

print()
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv # csv파일을 다루기위해서는 csv 모듈을 import 해야한다.

# 외부 CSV TO List of tuple

with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -')
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('EX2-2 -')
print(n_code1)

print()
print()

print('EX2-3 -')
print(n_code2)

print()
print()

# Dict Setdefault 예제 -> 이 함수 하나만 잘 사용해도 성능을 좋게 만들 수 있다.

source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}

# No use setdefault

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:    
        new_dict1[k] = [v]

print('EX3-1 -', new_dict1)

new_dict2 = {}

# Use setdefault -> dict의 setdefault 함수를 이용하면 위의 과정을 한번에 할 수 있고, 성능도 더 좋다고 한다.
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print('EX3-2 -', new_dict2)

# 사용자 정의 dict 상속(UserDict 가능)
# 자신만의 딕셔너리 클래스를 만들수 있다.
class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None): # 딕셔너리의 get 함수 호출시
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key): # 딕셔너리의 in 사용시
        print('Called :  __contains__')
        return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])

# 출력
print('EX4-1 -', user_dict1, user_dict2, user_dict3)
print('EX4-2 -', user_dict2.get('two')) # 2
print('EX4-2-1 -', user_dict2.get('dave')) # None
print('EX4-3 -', 'one' in user_dict3) # True
# print('EX4-4 -', user_dict3['three']) # KeyError 발생
print('EX4-5 -', user_dict3.get('three')) # None
print('EX4-6 -', 'three' in user_dict3) # False

print()
print()

# Immutable Dict
# 딕셔너리는 mutable이어서 값을 수정, 삭제가 가능하다.
# Immutable Dict은 딕셔너리를 한번 선언해 놓으면 절대 바꾸지 않을거야 라고 판단될때 사용한다.
# MappingProxyType를 사용해서 Immutable Dict을 만들 수 있다.
from types import MappingProxyType

d = {'Key1': 'TEST1'}

# Read Only -> 위의 딕셔너리를 immutable로 바꾸면은 오직 read만 가능하다.
d_frozen = MappingProxyType(d)

print('EX5-1 -', d, id(d))
print('EX5-2 -', d_frozen, id(d_frozen))
print('EX5-3 -', d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['Key1'] = 'TEST2' # 에러 발생
# d_frozen['Key2'] = 'TEST2' # 에러 발생

d['Key2'] = 'TEST2'
print('EX5-4 -', d)

# Set 구조(FrozenSet) : FronzenSet은 한번 할당을 하면 절대 수정, 추가, 삭제 불가하다.
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s3_1 = {} # 이거는 set이 아니라, 딕셔너리이다.
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')
print('EX6-1 -', s1, type(s1))

# 추가 불가
# s5.add('Melon') # 에러 발생

print('EX6-2 -', s2, type(s2))
print('EX6-3 -', s3, type(s3))
print('EX6-4 -', s4, type(s4))
print('EX6-5 -', s5, type(s5))

# 선언 최적화
# 같은 값을 가진 set이지만 선언 할때는 a처럼 선언을 하는 것이 성능이 좋다.
a = {10}
b = set([10])

# dis -> 이거는 이런게 있구나 하고 넘어가면 된다.
from dis import dis
print('EX6-5 -')
print(dis('{10}'))
print('EX6-6 -')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name # name 은 유니코드의 이름을 보여준다.

print('EX7-1 -')

print({name(chr(i), '') for i in range(0, 256)})