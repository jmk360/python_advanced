# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC : 추상 클래스

# class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x) # 언더바 2개를 쓰면 private이다. -> 직접 접근이 안된다.
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator

    @property
    def x(self): # 함수의 이름은 실제 변수의 이름으로 해주는 것이 좋다.
        print('Called Property x')
        return self.__x

    @x.setter # setter를 정의하기 전에는 반드시 getter를 먼저 정의해야 한다.
    def x(self, v):
        print('Called Property x Setter')
        self.__x = float(v)

    @property
    def y(self):
        print('Called Property y')
        return self.__y

    @y.setter
    def y(self, v):
        print('Called Property y Setter')
        if v < 30:
            raise ValueError('30 Below is not possible.')
        self.__y = float(v)

# 객체 선언
v = VectorP(20, 40)

# print('EX1-1 -', v.__x, v.__y) # private은 직접 접근이 안되기 때문에 에러가 발생한다.

# Getter, Setter
print('EX1-2 -', dir(v), v.__dict__)
print('EX1-3 -', v.x, v.y)

# Iter 확인
for val in v:
    print('EX1-4 -', val)

# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용
# 클래스에 어떤 속성을 사용할 것인지를 개발전에 미리 선정을 해놓고 설계를 잘 하고, 작업을 하면 매우 좋다.
# 하지만, 운영하다보면 새로운 것들이 추가가 된다. 그때는 속성을 dict형태로 관리하는 것이 유용할 수도있다.
# 클래스로 부터 객체를 많이 생성해야 하는 패키지나 프레임워크들을 보면 대부분 __slot__을 사용한다고 한다.
# __slots__를 사용하는게 __dict__ 사용하는 것보다 빠른데, 사이드 이팩트도 없고, 메모리도 덜 사용한다.

class TestA(object):
    __slots__ = ('a',) # 튜플안에 있는 놈만 속성으로 사용 가능하다.

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__) # 에러 발생
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'Test'
        del obj.a
    return repeat_inner

# print(min(timeit.repeat(repeat_outer(use_slot), number=50000)))
# print(min(timeit.repeat(repeat_outer(no_slot), number=50000)))

print()
print()

# 객체 슬라이싱

class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self): # len
        return len(self._numbers)

    def __getitem__(self, idx): # 인덱싱, 슬라이싱
        return self._numbers[idx]

s = ObjectS()

print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s))
print('EX3-3 -', len(s._numbers))
print('EX3-4 -', s[1:100])
print('EX3-5 -', s[-1])
print('EX3-6 -', s[::10])

print()
print()

# 파이썬 추상클래스
# 참고 : https://docs.python.org/3/library/collections.abc.html

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contain__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4:10])
print('EX4-3 -', 3 in i1[1:10]) # __contain__ 이놈을 구현을 안해났지만 python에서 getitem을 하면 자동으로 해준다.
print('EX4-4 -', [i for i in i1]) # __iter__ 이놈을 구현을 안해났지만 python에서 getitem을 하면 자동으로 해준다.

print()
print()

# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])
        

i2 = IterTestB()
print('EX4-5 -', i2[4])
print('EX4-6 -', i2[4:10])
print('EX4-7 -', 3 in i2[1:10])

# abc 활용 예제
import abc

# python 3.4 버전 이하 에서는 아래와 같이 추상클래스를 정의해야한다.
'''
class RandomMachine(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta
'''

class RandomMachine(abc.ABC): # 지금 추상클래스는 이거처럼 정의한다.

    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''

    # 추상 메소드
    @abc.abstractmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''
    
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crance Box')

    def __call__(self):
        return self.pick()

# 서브 클래스 확인
print('EX5-1 -', issubclass(RandomMachine, CraneMachine)) # issubclass로 서브클래스인지 확인가능하다.
print('EX5-2 -', issubclass(CraneMachine, RandomMachine))

# 상속 구조 확인
print('EX5-3 -', CraneMachine.mro())
print('EX5-3-1 -', CraneMachine.__mro__)

cm = CraneMachine(range(1, 100)) # 추상 메소드 구현 안하면 에러

print('EX5-4 -', cm._items)
print('EX5-5 -', cm.pick())
print('EX5-6 -', cm())
print('EX5-7 -', cm.inspect())